package practice;

import java.util.ArrayList;
import java.util.Scanner;

public class Cafe {
    private String name;
    private ArrayList<Coffee> menuList;

    public Cafe(String name) {
        this.name = name;
        this.menuList = new ArrayList<>();
    }

    public void addCoffee(Coffee coffee) {
        menuList.add(coffee);
    }

    public void showMenu() {
        System.out.println("어서오세요 " + name + " 입니다.");
        for (int i = 0; i < menuList.size(); i++) {
            System.out.println((i + 1) + ". " + menuList.get(i));
        }
    }

    public void buyCoffee(Scanner sc) {
        System.out.print("메뉴를 선택해주세요: ");
        int choice = sc.nextInt();
        if (choice > 0 && choice <= menuList.size()) {
            Coffee selectedCoffee = menuList.get(choice - 1);
            System.out.println(selectedCoffee.getName() + "을(를) " + selectedCoffee.getPrice() + "원에 구매했습니다.");
        } else {
            System.out.println("잘못된 선택입니다.");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 카페 생성
        Cafe starbucks = new Cafe("스타벅스");
        Cafe yaga = new Cafe("야가");

        // 스타벅스 메뉴 추가
        starbucks.addCoffee(new Coffee("아메리카노", 5000));
        starbucks.addCoffee(new Coffee("카푸치노", 6000));
        starbucks.addCoffee(new Coffee("오프라떼", 7000));

        // 야가 메뉴 추가
        yaga.addCoffee(new Coffee("아메리카노", 2500));
        yaga.addCoffee(new Coffee("바닐라라떼", 3000));
        yaga.addCoffee(new Coffee("아이스티", 3500));

        boolean run = true;

        while (run) {
            System.out.println("행동을 선택해주세요.");
            System.out.println("1. 스타벅스 방문 | 2. 야가 방문 | 3. 사무실 복귀..");
            System.out.print(">>> ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    starbucks.showMenu();
                    starbucks.buyCoffee(sc);
                    break;
                case 2:
                    yaga.showMenu();
                    yaga.buyCoffee(sc);
                    break;
                case 3:
                    System.out.println("사무실로 복귀합니다..");
                    run = false;
                    break;
                default:
                    System.out.println("잘못된 선택입니다.");
                    break;
            }
        }

        sc.close();
    }
}
