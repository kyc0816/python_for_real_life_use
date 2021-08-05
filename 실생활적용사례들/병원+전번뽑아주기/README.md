https://ncvr.kdca.go.kr/ 에서 마우스 우클릭 --> '검사' --> Network 탭 간 뒤...

우리 동네에서 병원 명단 불러오는 페이지까지 가면... 밑에 request url들 나오는데 그 중에서 살펴보면 response에
병원들 명단이 담겨있는게 하나 있다. 그 response를 긁어와서 json 파일로 만들고 format 해준 뒤 저장한다.

그리고 거기에서 내가 원하는, ${병원 이름} ${전화번호} 포맷으로 출력시키는 코드를 aa.py로 짰다.

venv 들어온 뒤 aa.py 실행시켜주면 된다.