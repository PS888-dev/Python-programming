# Capture Pattern ใช้ข้อมูลในตัวแปรมาอ้างอิงในการทำงาน
service=4
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงินคงเหลือ")
    case service: #นำค่าตัวแปรมาอ้างอิงในการทำงาน
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง")