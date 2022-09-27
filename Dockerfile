FROM python:3.10.7
WORKDIR /mnt/c/Users/acer/Documents/Teknologi-Sistem-Terintegrasi
ADD . /mnt/c/Users/acer/Documents/Teknologi-Sistem-Terintegrasi
CMD ["python", "test.py"]
