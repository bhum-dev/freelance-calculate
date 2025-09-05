def calculate_freelance_rate(monthly_salary, working_days=22, hours_per_day=8):
    """
    คำนวณอัตราค่าจ้างสำหรับ freelance ทั้งรายวันและรายชั่วโมง
    
    Parameters:
    monthly_salary: เงินเดือนปัจจุบัน
    working_days: จำนวนวันทำงานต่อเดือน (default: 22 วัน)
    hours_per_day: จำนวนชั่วโมงทำงานต่อวัน (default: 8 ชั่วโมง)
    
    Returns:
    dict: ข้อมูลการคำนวณอัตราค่าจ้างในรูปแบบต่างๆ
    """
    # ค่าใช้จ่ายพื้นฐานที่ต้องรับผิดชอบเอง
    insurance = 750  # ประกันสังคม/ประกันสุขภาพ
    equipment = 2000  # ค่าอุปกรณ์/ซอฟต์แวร์/อินเทอร์เน็ต
    
    # คำนวณค่าแรงพื้นฐานต่อวัน
    base_daily = monthly_salary / working_days
    base_hourly = base_daily / hours_per_day
    
    # เพิ่มค่าใช้จ่ายที่ต้องรับผิดชอบเอง
    adjusted_monthly = monthly_salary + insurance + equipment
    
    # คำนวณอัตราต่อวัน
    min_daily = (adjusted_monthly * 1.3) / working_days
    recommended_daily = (adjusted_monthly * 1.5) / working_days
    max_daily = (adjusted_monthly * 2) / working_days
    
    # คำนวณอัตราต่อชั่วโมง
    min_hourly = min_daily / hours_per_day
    recommended_hourly = recommended_daily / hours_per_day
    max_hourly = max_daily / hours_per_day
    
    return {
        "daily": {
            "base": round(base_daily),
            "minimum": round(min_daily),
            "recommended": round(recommended_daily),
            "maximum": round(max_daily)
        },
        "hourly": {
            "base": round(base_hourly),
            "minimum": round(min_hourly),
            "recommended": round(recommended_hourly),
            "maximum": round(max_hourly)
        }
    }

monthly_salary = 39000
# คำนวณสำหรับเงินเดือน 39,000 บาท
rates = calculate_freelance_rate(monthly_salary)


print(f"""
อัตราค่าจ้างต่อวันที่แนะนำสำหรับ Fullstack Developer สำหรับเงินเดือน {monthly_salary:,} บาท:
- อัตราพื้นฐาน: {rates['daily']['base']:,} บาท/วัน
- อัตราขั้นต่ำ: {rates['daily']['minimum']:,} บาท/วัน
- อัตราที่แนะนำ: {rates['daily']['recommended']:,} บาท/วัน
- อัตราสูงสุด: {rates['daily']['maximum']:,} บาท/วัน
""")

print(f"""
อัตราค่าจ้างต่อชั่วโมงที่แนะนำสำหรับ Fullstack Developer สำหรับเงินเดือน {monthly_salary:,} บาท:
- อัตราพื้นฐาน: {rates['hourly']['base']:,} บาท/ชั่วโมง
- อัตราขั้นต่ำ: {rates['hourly']['minimum']:,} บาท/ชั่วโมง
- อัตราที่แนะนำ: {rates['hourly']['recommended']:,} บาท/ชั่วโมง
- อัตราสูงสุด: {rates['hourly']['maximum']:,} บาท/ชั่วโมง
""")