

# ===========code by shakil munshi ===========================
# কেনাকাটার তালিকা: আপনি যখন বাজার করতে যান, তখন একটি লিস্ট বানান। এই লিস্টে নতুন জিনিস যোগ করা বা বাদ দেওয়া যায়।
shopping_lists= ["shakkjsdkjf","kfjklasjf;lkas","kadfkasjf"]
shopping_lists.append("ria")
print(shopping_lists)


# ===================code by shakiul munshi =================================
# শিক্ষার্থীদের রোল নম্বর: একটি ক্লাসের শিক্ষার্থীদের রোল নম্বরগুলো একটি লিস্টে সাজানো যায়।
roll_numbers = [1, 2, 3, 4, 5]
roll_numbers[2] = 6  # ৩ নম্বর রোল পরিবর্তন করে ৬ করা হলো
print(roll_numbers)  # আউটপুট: [1, 2, 6, 4, 5]



# ===================code by shakiul munshi =================================
# জন্ম তারিখ বা স্থানাঙ্ক: আপনার জন্ম তারিখ বা কোনো স্থানের অক্ষাংশ ও দ্রাঘিমাংশ কখনো পরিবর্তন হয় না।
birth_date = (1995, 12, 25)
# birth_date[0] = 2000  # এটি করলে error আসবে কারণ টুপল পরিবর্তন করা যায় না
print(birth_date)


# ===================code by shakiul munshi =================================
# সপ্তাহের দিনগুলো: সপ্তাহের দিনগুলো একটি নির্দিষ্ট ক্রমানুসারে থাকে এবং এটি পরিবর্তন হয় না।
weekdays = ("রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার")
print(weekdays[3])  # আউটপুট: রবিবার




# ===================code by shakiul munshi =================================
# শিক্ষার্থীদের তথ্য: একজন শিক্ষার্থীর নাম, রোল, ঠিকানা—এই তথ্যগুলো একটি ডিকশনারিতে রাখা যায়।
student = {
    "name": "আরিফ",
    "roll": 101,
    "class": "Five"
}
print(student["class"])  # আউটপুট: আরিফ


# ===================code by shakiul munshi =================================
# একটি ফোনবুক: আপনার মোবাইলের ফোনবুকে প্রতিটি নামের সাথে একটি ফোন নম্বর থাকে।
phone_book = {
    "mother": "017sdfasadfsda...",
    "brother": "018rewrweqrwe..."
}
print(phone_book["mother"])  # আউটপুট: 017...



# ===================code by shakiul munshi =================================
# একটি ক্লাসের শিক্ষার্থীদের নাম: একটি ক্লাসে দুজন শিক্ষার্থীর নাম একই হতে পারে না। যদি থাকেও, সেটে শুধুমাত্র একটি নামই থাকবে।
class_students = {"আসিফ", "তানিয়া", "রনি", "আসিফ"}
print(class_students)  # আউটপুট: {'রনি', 'আসিফ', 'তানিয়া'} - দেখুন, 'আসিফ' একবারই আছে।

# ===================code by shakiul munshi =================================
# ১ থেকে ১০ পর্যন্ত সংখ্যাগুলোর বর্গ:
# ১ থেকে ১০ পর্যন্ত সংখ্যাগুলোর বর্গ:
# ১ থেকে ১০ পর্যন্ত সংখ্যাগুলোর বর্গ:

# সাধারণ পদ্ধতি
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# ===================code by shakiul munshi =================================
# একটি লিস্ট থেকে শুধুমাত্র জোড় সংখ্যাগুলো বের করা:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # আউটপুট: [2, 4, 6, 8, 10]


# File Handling (ফাইল হ্যান্ডলিং)
# বৈশিষ্ট্য: ফাইল থেকে ডেটা পড়া বা ফাইলে নতুন ডেটা লেখা। with open() ব্যবহার করলে ফাইলটি কাজ শেষে স্বয়ংক্রিয়ভাবে বন্ধ হয়ে যায়।
# উদাহরণ:

# একটি ফাইলে কিছু লেখা এবং তারপর তা পড়া:

# লেখা (write)
with open("notes.txt", "w") as file:
    file.write("আজকের তারিখ: 5 আগস্ট 2025\n")
    file.write("ক্লাসটি খুব ভালো ছিল।")

# পড়া (read)
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


    with open("notes.text", "w") as file:
      file.writeI

    # ===================code by shakiul munshi =================================
    # শূন্য দিয়ে ভাগ করা:


try:
    result = 10 / 0  # এটি একটি ZeroDivisionError
except ZeroDivisionError:
    print("ভুল! কোনো সংখ্যাকে শূন্য দিয়ে ভাগ করা যায় না।")


 # ===================code by shakiul munshi =================================
    # একটি লিস্টের বাইরে থেকে ডেটা অ্যাক্সেস করার চেষ্টা:

    my_list = [1, 2, 3]
try:
    print(my_list[5])  # এই indexটি লিস্টে নেই, তাই IndexError আসবে
except IndexError:
    print("ভুল! আপনি একটি অ-বিদ্যমান index থেকে ডেটা নেওয়ার চেষ্টা করছেন।")


 # ===================code by shakiul munshi =================================
# 🔧 মিনি প্রজেক্ট: Student Report Card System
# এই প্রজেক্টটি উপরের সব ধারণাগুলো একত্রিত করে একটি চমৎকার উদাহরণ তৈরি করবে।

# ফাইল তৈরি করা: students.txt
# প্রথমে একটি ফাইল তৈরি করুন যেখানে শিক্ষার্থীদের ডেটা থাকবে।

def generate_report_card():
    # ফাইল থেকে ডেটা পড়ার জন্য Exception Handling ব্যবহার
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("--- শিক্ষার্থী রিপোর্ট কার্ড ---")
        
        # প্রথম লাইনটি (হেডার) বাদ দেওয়া
        for line in lines[1:]:
            # প্রতি লাইনের শেষে থাকা নতুন লাইন অক্ষরটি মুছে ফেলা
            data = line.strip().split(',') 
            
            # ডেটাগুলোকে সাজানো
            name = data[0]
            roll = data[1]
            math = int(data[2])
            bangla = int(data[3])
            english = int(data[4])
            
            # মোট নম্বর এবং গড় হিসাব করা
            total_marks = math + bangla + english
            average_marks = total_marks / 3
            
            # রিপোর্ট কার্ড প্রিন্ট করা
            print(f"\nনাম: {name} (রোল: {roll})")
            print(f"গণিত: {math}, বাংলা: {bangla}, ইংরেজি: {english}")
            print(f"মোট নম্বর: {total_marks}")
            print(f"গড় নম্বর: {average_marks:.2f}")

    except FileNotFoundError:
        print("ভুল! 'students.txt' ফাইলটি খুঁজে পাওয়া যায়নি।")
    except Exception as e:
        print(f"একটি অপ্রত্যাশিত ত্রুটি ঘটেছে: {e}")

# ফাংশনটি কল করে প্রোগ্রাম চালানো
generate_report_card()