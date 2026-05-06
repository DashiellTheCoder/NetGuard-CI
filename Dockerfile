# 1. The Base OS: Like choosing a lightweight Linux Distro
FROM python:3.11-alpine

# 2. The Directory: Like 'mkdir app && cd app'
WORKDIR /app

# 3. Dependencies: Like 'npm install'
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. The Code: Copying your files into the 'box'
COPY . .

# 5. SECURITY: Create a limited user (The SANS Scholarship winner move)
# This prevents a hacker from being 'Admin' if they break your script.
RUN adduser -D netuser
USER netuser

# 6. Execution: What happens when the box opens
CMD ["python", "monitor.py"]