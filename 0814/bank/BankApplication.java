package bank;

import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

import javax.security.auth.login.AccountNotFoundException;

public class BankApplication {

    public static void main(String[] args) {
        bank();
    }

    public static void bank() {
        Scanner scan = new Scanner(System.in);
        boolean run = true;

        while (run) {
            System.out.println("\n[은행]");
            System.out.println("1. 계좌 생성 | 2. 계좌 목록 | 3. 예금 | 4. 출금 | 5. 종료");
            System.out.print("선택 >> ");
            
            int number = scan.nextInt();
            scan.nextLine(); // nextInt() 후 남은 개행문자 제거

            switch (number) {
                case 1:
                    System.out.println("계좌 생성");
                    System.out.println("");

                    try {
                        System.out.print("계좌번호: ");
                        String accountNum = scan.nextLine(); // 계좌번호 입력

                        System.out.print("계좌주: ");
                        String name = scan.nextLine(); // 계좌주 입력

                        System.out.print("초기입금액: ");
                        int balance = scan.nextInt(); // 초기입금액 입력

                        Account account = new Account(accountNum, name, balance);

                        System.out.println("결과 : 계좌가 생성되었습니다.");

                    } catch (InputMismatchException e) {
                        System.out.println("결과 : 잘못된 입력입니다. 초기 입금액은 숫자여야 합니다.");
                        scan.nextLine();
                    } catch (Exception e) {
                        System.out.println("결과 : 계좌 생성 중 오류가 발생했습니다: \n" + e.getMessage());
                    }
                    break;

                case 2:
                    System.out.println("계좌 목록");
                    List<Account> allAccounts = Account.getAllAccounts();
                    for (Account account : allAccounts) {
                        System.out.println(account);
                    }
                    break;

                case 3:
                    System.out.println("예금");
                    try {
                        System.out.print("계좌번호: ");
                        String accountNum = scan.nextLine(); 
                        
                        System.out.print("금액: ");
                        int balance = scan.nextInt(); 

                        Account account = Account.findAccountByNumber(accountNum);
                        
                        if(account == null)
                        {
                        	 throw new AccountNotFoundException("해당 계좌번호를 가진 계좌를 찾을 수 없습니다: " + accountNum);
                        }else if(0 > balance) {
                        	System.out.println("입금액은 자연수 숫자여야 합니다.");
                        }else {
                        	System.out.println("예금 : " + balance);
                        	account.setBalance(account.getBalance()+balance);
                        }

                    } catch (Exception e) {
                        System.out.println("결과 : 예금 중 오류가 발생했습니다: \n" + e.getMessage());
                    }
                    break;

                case 4:
                    System.out.println("출금");
                    try {
                        System.out.print("계좌번호: ");
                        String accountNum = scan.nextLine(); 
                        
                        System.out.print("금액: ");
                        int balance = scan.nextInt(); 

                        Account account = Account.findAccountByNumber(accountNum);
                        
                        if(account == null)
                        {
                        	 throw new AccountNotFoundException("해당 계좌번호를 가진 계좌를 찾을 수 없습니다: " + accountNum);
                        }else if(0 > balance) {
                        	System.out.println("출금액은 자연수 숫자여야 합니다.");
                        }else if(account.getBalance() < balance) {
                        	System.out.println("출금액은 잔액보다 작아야 합니다.");
                        }else {
                        	System.out.println("출금 : " + balance);
                        	account.setBalance(account.getBalance()-balance);
                        }

                    } catch (Exception e) {
                        System.out.println("결과 : 예금 중 오류가 발생했습니다: \n" + e.getMessage());
                    }
                    break;

                case 5:
                    run = false;
                    System.out.println("종료");
                    break;

                default:
                    System.out.println("올바른 메뉴를 선택하세요.");
            }
        }
        
        scan.close(); // 스캐너 자원 해제
    }
}
