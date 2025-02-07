import requests
import datetime
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label, Toplevel
from PIL import Image, ImageTk
import cv2
import threading
from pyzbar.pyzbar import decode

# ✅ API 정보
BASE_URL = "http://assets.woowa.in/x1/api/help-desk/assets"
API_KEY = "Bearer help-desk-2e503c87-492f-4665-9a45-9a5517aa2e76"  # 🔹 API 키 입력
USER_NUMBER = "23080058"  # 🔹 조회할 유저 사번

headers = {
    "Authorization": API_KEY,
    "asset-user-number": USER_NUMBER
}

# ✅ 경로 설정
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# ✅ 창 생성
window = Tk()
window.geometry("1920x1080")
window.configure(bg="#F5F5F5")

# ✅ 캔버스 생성
canvas = Canvas(
    window,
    bg="#F5F5F5",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# ✅ 첫 번째 화면 UI 요소
image_logo = PhotoImage(file=relative_to_assets("frame3/image_1.png"))
img_label_logo = Label(window, image=image_logo, bg="#F5F5F5")
img_label_logo.place(x=960.0, y=415.0, anchor="center")

main_title_1 = canvas.create_text(
    694.0, 546.0, anchor="nw", text="노후장비 개인구매",
    fill="#000000", font=("Noto Sans KR Bold", -70)
)
main_title_2 = canvas.create_text(
    694.0, 648.0, anchor="nw", text="₩10,000부터",
    fill="#66666D", font=("Noto Sans KR Medium", -35)
)

main_button = PhotoImage(file=relative_to_assets("frame3/button_1.png"))
button_1 = Button(
    image=main_button, borderwidth=0, highlightthickness=0,
    command=lambda: switch_to_second_frame(), relief="flat"
)
button_1.place(x=694.0, y=774.0, width=532.0, height=48.0)

main_title_3 = canvas.create_text(
    694.0, 840.0, anchor="nw", text="시간이 좀 더 필요하신가요?",
    fill="#000000", font=("Noto Sans KR Medium", 20 * -1)
)

main_title_4 = canvas.create_text(
    694.0, 874.0, anchor="nw", text="신규 장비 수령 후 2주가 지나면 구매 기회가 사라집니다.",
    fill="#66666D", font=("Noto Sans KR Medium", 18 * -1)
)

# ✅ 두 번째 화면 UI 요소 (초기에 숨김)
shared_background = PhotoImage(file=relative_to_assets("frame2/image_1.png"))
background_1 = canvas.create_image(354.0, 653.0, anchor="center", image=shared_background)
background_2 = canvas.create_image(960.0, 653.0, anchor="center", image=shared_background)
background_3 = canvas.create_image(1566.0, 653.0, anchor="center", image=shared_background)

title_1 = canvas.create_text(
    102.0, 98.0, anchor="nw", text="노후장비 개인구매.",
    fill="#000000", font=("Noto Sans KR Bold", 70 * -1)
)

title_2 = canvas.create_text(
    668.0, 98.0, anchor="nw", text="네꺼에서",
    fill="#66666D", font=("Noto Sans KR Bold", 70 * -1)
)

title_3 = canvas.create_text(
    107.0, 199.0, anchor="nw", text="내꺼로",
    fill="#66666D", font=("Noto Sans KR Bold", 70 * -1)
)

# ✅ Step 1
step1_title_1 = canvas.create_text(
    107.0, 390.0, anchor="nw", text="구매할 노후 노트북 선택",
    fill="#000000", font=("Noto Sans KR Bold", 40 * -1)
)

step1_title_2 = canvas.create_text(
    107.0, 451.0, anchor="nw", text="QR 코드를 입력해주세요",
    fill="#66666D", font=("Noto Sans KR Bold", 20 * -1)
)

qr_input = PhotoImage(file=relative_to_assets("frame2/image_6.png"))

# ✅ step1_assetnumber (초기 숨김)
step1_assetnumber = canvas.create_text(
    107.0, 790.0, anchor="nw", text="",
    fill="#66666D", font=("Noto Sans KR Bold", 15 * -1)
)

step1_categoryName = canvas.create_text(
    107.0, 817.0, anchor="nw", text="",
    fill="#000000", font=("Noto Sans KR Bold", 30 * -1)
)

step1_userinfo = canvas.create_text(
    107.0, 905.0, anchor="nw", text="",
    fill="#66666D", font=("Noto Sans KR Bold", 15 * -1)
)

step1_sapEstimatedPrice = canvas.create_text(
    107.0, 864.0, anchor="nw", text="",
    fill="#66666D", font=("Noto Sans KR Bold", 25 * -1)
)

canvas.itemconfig(step1_assetnumber, state='hidden') 
canvas.itemconfig(step1_categoryName, state='hidden')  
canvas.itemconfig(step1_userinfo, state='hidden') 
canvas.itemconfig(step1_sapEstimatedPrice, state='hidden')  


def open_qr_scanner():
    """
    QR 코드 스캐너 창을 실행하는 함수
    """
    scanner_window = Toplevel(window)  # ✅ 새 창 생성
    scanner_window.title("q를 누를 경우 종료됩니다")  # ✅ 창 제목 설정
    scanner_window.geometry("500x500")  # ✅ 창 크기 (정사각형 1:1 비율)
    scanner_window.attributes("-topmost", True)  # ✅ 창을 항상 맨 앞으로 설정

    # ✅ 화면 중앙 배치
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width // 2) - (500 // 2)  # 중앙 정렬 X 좌표
    y_position = (screen_height // 2) - (500 // 2)  # 중앙 정렬 Y 좌표
    scanner_window.geometry(f"500x500+{x_position}+{y_position}")

    # ✅ OpenCV 카메라 실행 (새 창에서 실행)
    threading.Thread(target=lambda: read_qr_code(scanner_window)).start()

# ✅ QR 코드 인식 함수
def read_qr_code(scanner_window):
    """
    QR 코드를 인식하고 결과를 UI에 반영하는 함수
    """
    cap = cv2.VideoCapture(0)  # ✅ 기본 카메라 열기
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  # ✅ 1:1 비율 (정사각형)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    qr_data = None  # ✅ 초기값 설정

    # ✅ OpenCV 영상을 표시할 Canvas
    canvas_label = Canvas(scanner_window, width=480, height=480)
    canvas_label.pack()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 열 수 없습니다.")
            break

        # ✅ QR 코드 분석
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8").strip()
            if qr_data and not qr_data.startswith("WARNING"):
                print(f"📌 QR 코드 인식: {qr_data}")

                cap.release()
                cv2.destroyAllWindows()
                scanner_window.destroy()  # ✅ 창 닫기
                return

        # ✅ OpenCV 영상을 Tkinter 창에 표시
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        canvas_label.create_image(0, 0, anchor="nw", image=imgtk)
        canvas_label.image = imgtk  # ✅ 이미지 참조 유지

        scanner_window.update()  # ✅ 창 업데이트



# ✅ API 요청 함수
def find_serial_number(assets, asset_id):
    for asset in assets:
        if asset.get("assetId") == asset_id:
            return asset.get("serialNumber")
    return None

def get_asset_details_by_qr(asset_id):
    url_1 = f"{BASE_URL}/all"
    try:
        response = requests.get(url_1, headers=headers)
        if response.status_code == 200:
            assets = response.json().get("data", [])
            serial_number = find_serial_number(assets, asset_id)
            
            if not serial_number:
                print("⚠️ 해당 자산번호를 찾을 수 없습니다.")
                return None

            print(f"✅ 찾은 serialNumber: {serial_number}")

            url_2 = f"{BASE_URL}/{serial_number}"
            response = requests.get(url_2, headers=headers)
            if response.status_code == 200:
                return response.json().get("data", {})
            else:
                print(f"❌ 두 번째 API 요청 실패! 상태 코드: {response.status_code}")
                return None
        else:
            print(f"❌ 첫 번째 API 요청 실패! 상태 코드: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ API 요청 중 오류 발생: {e}")
        return None

# ✅ QR 코드 버튼 클릭 이벤트
qr_input_button = Button(
    image=qr_input, borderwidth=0, highlightthickness=0,
    command=open_qr_scanner,  # ✅ QR 코드 실행 (새 창)
    relief="flat"
)

# ✅ QR 코드 UI 업데이트 함수
def update_ui_with_asset_details(asset_id):
    asset_data = get_asset_details_by_qr(asset_id)
    if not asset_data:
        print("⚠️ 자산 정보를 가져올 수 없습니다.")
        return

    category_name = asset_data.get("categoryName", "N/A")
    sap_estimated_price = asset_data.get("sapEstimatedPrice", "N/A")
    user_name = asset_data.get("userName", "N/A")
    department_name = asset_data.get("departmentName", "N/A")
    assigned_datetime = asset_data.get("assignedDateTime", "N/A")

    try:
        assigned_date = datetime.datetime.strptime(assigned_datetime, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
    except ValueError:
        assigned_date = assigned_datetime
    
    assigned_date = assigned_date.split("T")[0]

    user_info_text = f"{user_name} ({department_name}), {assigned_date} 지급"

    canvas.itemconfig(step1_assetnumber, text=asset_id, state='normal')
    canvas.itemconfig(step1_categoryName, text=category_name, state='normal')
    canvas.itemconfig(step1_sapEstimatedPrice, text=f"{int(sap_estimated_price):,} 원", state='normal')
    canvas.itemconfig(step1_userinfo, text=user_info_text, state='normal')





# ✅ QR 코드 인식 함수
def read_qr_code(scanner_window):
    """
    QR 코드를 인식하고 결과를 UI에 반영하는 함수
    """
    cap = cv2.VideoCapture(0)  # ✅ 기본 카메라 열기
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)  # ✅ 1:1 비율 (정사각형)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    qr_data = None  # ✅ 초기값 설정

    # ✅ OpenCV 영상을 표시할 Canvas
    canvas_label = Canvas(scanner_window, width=480, height=480)
    canvas_label.pack()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 열 수 없습니다.")
            break

        # ✅ QR 코드 분석
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8").strip()
            if qr_data and not qr_data.startswith("WARNING"):
                print(f"📌 QR 코드 인식: {qr_data}")

                cap.release()
                cv2.destroyAllWindows()
                scanner_window.destroy()  # ✅ 창 닫기
                update_ui_with_asset_details(qr_data)
                return

        # ✅ OpenCV 영상을 Tkinter 창에 표시
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        canvas_label.create_image(0, 0, anchor="nw", image=imgtk)
        canvas_label.image = imgtk  # ✅ 이미지 참조 유지

        scanner_window.update()  # ✅ 창 업데이트

# ✅ 화면 전환 함수
def switch_to_second_frame():
    img_label_logo.place_forget()
    canvas.itemconfig(main_title_1, state='hidden')
    canvas.itemconfig(main_title_2, state='hidden')
    canvas.itemconfig(main_title_3, state='hidden')
    canvas.itemconfig(main_title_4, state='hidden')
    button_1.place_forget()
    
    # ✅ 두 번째 화면 표시
    canvas.itemconfig(title_1, state='normal')
    canvas.itemconfig(title_2, state='normal')
    canvas.itemconfig(title_3, state='normal')
    canvas.itemconfig(background_1, state='normal')
    canvas.itemconfig(background_2, state='normal')
    canvas.itemconfig(background_3, state='normal')
    canvas.itemconfig(step1_title_1, state='normal')
    canvas.itemconfig(step1_title_2, state='normal')
    qr_input_button.place(x=353.0, y=653.0, anchor="center")

# ✅ 두 번째 화면 요소 초기 숨김 처리
canvas.itemconfig(background_1, state='hidden')
canvas.itemconfig(background_2, state='hidden')
canvas.itemconfig(background_3, state='hidden')
canvas.itemconfig(step1_title_1, state='hidden')
canvas.itemconfig(step1_title_2, state='hidden')
canvas.itemconfig(title_1, state='hidden')
canvas.itemconfig(title_2, state='hidden')
canvas.itemconfig(title_3, state='hidden')
qr_input_button.place_forget()

window.resizable(False, False)
window.mainloop()
