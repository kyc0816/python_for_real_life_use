num_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_year(year, print_year_too):
	if print_year_too:
		for month in range(1, 13):
			for day in range(1, num_days_in_month[month-1]+1):
				print(f'{year}년 {month}월{day}일')
	else:
		print(f'----{year}년----')
		for month in range(1, 13):
			for day in range(1, num_days_in_month[month-1]+1):
				print(f'{month}월{day}일')

years = [2021, 2022, 2023]
def dats_in_years(years, print_year_too):
	for year in years:
		days_in_year(year, print_year_too)

do_continue = True
while do_continue:
	print('몇년도 날짜를 뽑으시겠습니까? (종료하려면 Q를 입력하세요)')
	input_year = input()
	if input_year == 'Q':
		break
	print('연도도 같이 출력하기 원하십니까? (Y/N)')
	input_print_year_too = input()
	if input_print_year_too == 'Y':
		days_in_year(int(input_year), True)
	elif input_print_year_too == 'N':
		days_in_year(int(input_year), False)
	else:
		print("잘못 입력하셨습니다. 처음부터 다시 합니다.\n-----------------------------------------\n")