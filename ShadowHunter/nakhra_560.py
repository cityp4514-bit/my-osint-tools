import math
import datetime

def calculator():
    print("=" * 40)
    print("   آلة حاسبة متطورة")
    print("=" * 40)
    print("العمليات المتاحة:")
    print("  1. جمع (+)")
    print("  2. طرح (-)")
    print("  3. ضرب (*)")
    print("  4. قسمة (/)")
    print("  5. الأس (**)")
    print("  6. الجذر التربيعي (√)")
    print("  7. النسبة المئوية (%)")
    print("  8. تحويل العملات (USD->SAR)")
    print("=" * 40)

    history = []

    while True:
        try:
            # اختيار العملية
            choice = input("\nاختر العملية (1-8) أو 'q' للخروج: ").strip()

            if choice.lower() == 'q':
                break

            # العمليات التي تحتاج رقمين
            if choice in ['1', '2', '3', '4', '5', '8']:
                num1 = float(input("أدخل الرقم الأول: "))
                num2 = float(input("أدخل الرقم الثاني: "))

                if choice == '1': result = num1 + num2
                elif choice == '2': result = num1 - num2
                elif choice == '3': result = num1 * num2
                elif choice == '4':
                    if num2 == 0:
                        print("⚠️ لا يمكن القسمة على صفر!")
                        continue
                    result = num1 / num2
                elif choice == '5': result = num1 ** num2
                elif choice == '8': result = num1 * 3.75  # تحويل USD إلى SAR

                print(f"✅ النتيجة: {num1} {['+','-','*','/','**','->'][int(choice)-1]} {num2} = {result}")

            # العمليات التي تحتاج رقم واحد
            elif choice == '6':
                num = float(input("أدخل الرقم: "))
                result = math.sqrt(num)
                print(f"✅ الجذر التربيعي لـ {num} = {result}")

            elif choice == '7':
                num1 = float(input("أدخل الرقم: "))
                num2 = float(input("أدخل النسبة المئوية: "))
                result = (num1 * num2) / 100
                print(f"✅ {num2}% من {num1} = {result}")

            else:
                print("⚠️ خيار غير صالح!")
                continue

            # حفظ التاريخ
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append(f"[{timestamp}] {result}")

            # عرض الخيارات
            again = input("\nهل تريد متابعة؟ (y/n): ").lower()
            if again != 'y':
                break

        except ValueError:
            print("⚠️ يرجى إدخال أرقام صحيحة!")
        except Exception as e:
            print(f"⚠️ حدث خطأ: {e}")

    # عرض تاريخ العمليات
    if history:
        print("\n📋 تاريخ العمليات:")
        for entry in history:
            print(f"   {entry}")

# تشغيل الآلة الحاسبة
calculator()
