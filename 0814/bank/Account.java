package bank;

import java.util.ArrayList;
import java.util.List;

import javax.security.auth.login.AccountNotFoundException;

public class Account {
	
    private static List<Account> accountList = new ArrayList<>();
    private static int nextId = 1;
    private int id;
	private String accountNum;
	private String name;
	private int balance;


	public int getId() {
		return id;
	}

	public String getAccountNum() {
		return accountNum;
	}

	public void setAccountNum(String accountNum) {
		this.accountNum = accountNum;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getBalance() {
		return balance;
	}

	public void setBalance(int balance) {
		this.balance = balance;
	}
	
    public static List<Account> getAllAccounts() {
        return accountList;
    }

    public Account() {
        this(null, null, 0);
    }

    public Account(String accountNum, String name, int balance) {
        this.id = nextId++;
        this.accountNum = accountNum;
        this.name = name;
        this.balance = balance;
        accountList.add(this);
    }



    @Override
    public String toString() {
        return "Account [id=" + id + ", accountNum=" + accountNum + ", name=" + name + ", balance=" + balance + "]";
    }
    
    public static Account findAccountByNumber(String accountNum) throws AccountNotFoundException {
        for (Account account : accountList) {
            if (account.getAccountNum().equals(accountNum)) {
                return account;
            }
        }
        return null;
    }



    public static void main(String[] args) {
        Account acc1 = new Account("123-456-789", "test1", 1000);
        Account acc2 = new Account("987-654-321", "test2", 2000);
        Account acc3 = new Account();

        System.out.println(acc1); 
        System.out.println(acc2);
        System.out.println(acc3);
        
        
        List<Account> allAccounts = Account.getAllAccounts();
        System.out.println("\n전체 계좌 목록:");
        for (Account account : allAccounts) {
            System.out.println(account);
        }
    }

}
