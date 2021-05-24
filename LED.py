import RPi.GPIO as GPIO
 
 # time 라이브러리 임포트
 import time

 # 핀번호 할당법은 커넥터 핀번호로 설정
 GPIO.setmode(GPIO.BOARD)
 
 # 사용할 핀번호 대입
 LED = 11
 
 # 11번 핀을 출력 핀으로 설정, 초기출력은 로우레벨
 GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
 GPIO.output(LED, GPIO.HIGH)
 time.sleep(10)
