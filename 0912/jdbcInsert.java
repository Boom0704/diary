package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbcInsert {

	public static void main(String[] args) {
		
		
		Connection conn = null;
		
		PreparedStatement ps = null;
		
		ResultSet rs = null;	
		
	try {
		
		Class.forName("oracle.jdbc.driver.OracleDriver");
		System.out.println("드라이버 등록 성공");
	}
	catch (ClassNotFoundException e)
	{
		System.out.println("등록 실패");
		e.printStackTrace();
		System.exit(0);
	}
	
	String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
	String db_id = "member"; 
	String db_pw = "member";
	
	try {
		conn = DriverManager.getConnection(url, db_id, db_pw);
		System.out.println("접속 성공");
		
		StringBuffer query = new StringBuffer();
		query.append("");
		query.append("INSERT INTO 학생 (학번, 이름, 주소, 전공, 부전공, 생년월일, 학기, 평점)");
		query.append(" VALUES (?, ?, ?, ?, ?, TO_DATE(?, 'YYYY/MM/DD'), ?, ?)");
		System.out.println(query);
		
		ps = conn.prepareStatement(query.toString());
	
		System.out.println("1");
		ps.setString(1,"1111111111");
		
		System.out.println("2");
		
		ps.setString(2,"팽수");
		
		System.out.println("3");
		
		ps.setString(3,"EBS");
		
		System.out.println("4");
		
		ps.setString(4,"방송통신과");
		
		System.out.println("5");
		
		ps.setString(5,"연기과");
		
		System.out.println("6");
		
		ps.setString(6, "2000/01/01"); 
		
		System.out.println("7");
		
		ps.setInt(7,1);
		
		System.out.println("8");
		
		ps.setNull(8, java.sql.Types.FLOAT); 
		
		System.out.println("9");
		
		int count = ps.executeUpdate();  
		
		System.out.println("10");
		
		System.out.println("Rows affected: " + count);
	}
	catch(SQLException e)
	{
		e.printStackTrace();
	} finally
	{
		if (rs != null)
		{
			try {
				rs.close();
			}catch(SQLException e)
			{
				e.printStackTrace();
			}
		}
		
		if (ps != null)
		{
			try {
				ps.close();
			}catch(SQLException e)
			{
				e.printStackTrace();
			}
		}
		
		if (conn != null)
		{
			try {
				conn.close();
			}catch(SQLException e)
			{
				e.printStackTrace();
			}
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	}

}