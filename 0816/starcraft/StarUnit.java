package ch10_extens_interface.starcraft;

public class StarUnit {
	
	private String name;
	private int damage;
	private int hp;
	private int armor;
	
	public void move(int x, int y) {
		System.out.println(name + "이(가) x:" + x + ", y:" + y + "로 이동");
	}
	public void attack(StarUnit unit) {
		// 대상 유닛에 해당 유닛의 damage만큼 손상되도록
		unit.setHp(unit.getHp() - damage);
	}
	// 1.기본, 필드있는 생성자 생성
	// 2.toString 재정의
	// 3.setter getter 생성
	public StarUnit() {
		super();
	}
	public StarUnit(String name, int damage, int hp, int armor) {
		super();
		this.name = name;
		this.damage = damage;
		this.hp = hp;
		this.armor = armor;
	}
	@Override
	public String toString() {
		return "StarUnit [name=" + name + ", damage=" + damage + ", hp=" + hp + ", armor=" + armor + "]";
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getDamage() {
		return damage;
	}
	public void setDamage(int damage) {
		this.damage = damage;
	}
	public int getHp() {
		return hp;
	}
	public void setHp(int hp) {
		this.hp = hp;
	}
	public int getArmor() {
		return armor;
	}
	public void setArmor(int armor) {
		this.armor = armor;
	}
	
	
}
