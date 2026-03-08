# ১. পাইথন ইমেজ ব্যবহার করা
FROM python:3.10-slim

# ২. ডিরেক্টরি সেট করা
WORKDIR /app

# ৩. প্রয়োজনীয় লাইব্রেরি কপি ও ইনস্টল করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ৪. সব কোড কপি করা
COPY . .

# ৫. পোর্ট এক্সপোজ করা
EXPOSE 8000

# ৬. সার্ভার চালু করার কমান্ড
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
