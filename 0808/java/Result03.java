package practice;

import java.util.Scanner;

/**
 * class Name : Result03
 * Author : Boom
 * Created Date : 2024. 8. 8.
 * Version : 1.0
 * Purpose : 숫자 맞추기 기회는 5번
 * Description : 
 */
public class Result03 {

	public static void main(String[] args) {
		int randInt = (int) (Math.random() * 50 + 1);
//		System.out.println(randInt);
		int chance = 5;

		guess(chance, randInt);

	}
	public static void guess(int chance, int randInt) {
		if(chance == 0) {
			System.out.printf("실패하셨습니다. 정답은 %d입니다. %n", randInt);
			return;
		}
		
		Scanner scan = new Scanner(System.in);
		System.out.println("숫자를 입력해주세요 : ");
		int number = scan.nextInt();
		if(number == randInt) {
			System.out.println("정답입니다.");
		}else if(number > randInt) {
			System.out.printf("다운!! 기회가 %d번 남았습니다.%n", chance - 1);
			guess(chance - 1, randInt);
		}else if(number < randInt) {
			System.out.printf("업!! 기회가 %d번 남았습니다.%n", chance - 1);
			guess(chance - 1, randInt);
		}
	}
}
