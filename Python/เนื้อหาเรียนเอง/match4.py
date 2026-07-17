# Litterlal Pattern กำหนดการทำงานนำค่าในตัวแปรมาตรวจสอบ ค่าตัวแปรเป็นค่าคงที่
service=1
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงินคงเหลือ")
    case None:
        print("ข้อมูลไม่ถูกต้อง")
