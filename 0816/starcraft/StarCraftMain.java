package ch10_extens_interface.starcraft;

public class StarCraftMain {

	public static void main(String[] args) {
		
		Marine marine01 = new Marine();
		Marine marine02 = new Marine("영웅마린", 8, 100, 0);
		System.out.println(marine01);
		System.out.println(marine02);
		
		marine02.move(100, 200);
		marine02.stimpack();
		System.out.println(marine02);

	}

}
