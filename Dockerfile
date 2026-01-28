# A Dockerfile should be minimal, reproducible, and explicit about how your app runs.

#Base Image - Uses an official Python 3.11 Docker image
FROM python:3.11-slim-buster

#Workdir - Sets /app as the default directory inside the containerAll future commands (RUN, CMD, COPY) runrelative to /app. Avoids absolute paths everywhere. If /app doesn’t exist → Docker creates it'''
WORKDIR /app

#Copy - copies the source code from your local folder (where the Dockerfile is) into /app inside the container.
COPY . /app

#Run - Runs during image build. Installs Python dependencies into the image. If app code changes but requirements.txt doesn’t → Docker reuses cached layer.
RUN pip install --no-cache-dir -r requirements.txt

#Port - Documents which port the container listens on. Streamlit defaults to 8501
EXPOSE 8501

#Commands - Docker requires JSON array with double quotes. This is usually the command seperated with quotes. streamlit run streamlit.py use 0.0.0.0 because without it, Streamlit binds to localhost, and the container wont be accessible from outside'''
CMD ["streamlit", "run", "streamlit.py", "--server.port=8051", "--server.address=0.0.0.0"]