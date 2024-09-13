package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbcSelect {

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
		query.append("Select * from 학생");
		
		System.out.println(query);
		
		ps = conn.prepareStatement(query.toString());
		rs = ps.executeQuery();
		
		while(rs.next())
		{
			int num = rs.getInt("학번");
			String rm = rs.getString("이름");
			System.out.println("학번 : " + num + " 이름 : " + rm +"\n");
			
		}
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
		
		if (rs != null)
		{
			try {
				ps.close();
			}catch(SQLException e)
			{
				e.printStackTrace();
			}
		}
		
		if (rs != null)
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
