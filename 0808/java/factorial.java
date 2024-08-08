package method;

/**
 * class Name : q2
 * Author : Boom
 * Created Date : 2024. 8. 8.
 * Version : 1.0
 * Purpose : 팩토리얼 사용
 * Description : 10!와 15!를 출력
 */
public class q2 {

	public static void main(String[] args) {
		long result1 = factorial(10);
//		System.out.println("1");
//		long result2 = factorial(10,0);
	}
	
	public static long factorial(int value) {
		long num = 1;
		long result = factorial(value-1, num * value);
//		System.out.println(result);
		return result;
	}
	public static long factorial(int value, long middle) {
		System.out.println(middle);
		if(value == 1) {
			return middle;
		}
		long result = factorial(value-1, middle * value);
		return result;
	}
}
