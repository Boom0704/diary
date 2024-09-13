package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class jdbcUpdate {

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
		query.append(" update 학생");
		query.append(" SET 학번 = 1111111122");
		query.append(" where 이름 = ?");
		
		System.out.println(query);
		
		ps = conn.prepareStatement(query.toString());
		ps.setString(1,"이원호");
		//rs = ps.executeQuery();
		
		int cnt = ps.executeUpdate();
		
		if(cnt > 0)
		{
			System.out.println(cnt + "건 수정함");
		}
		else
		{
			System.out.println("대상건이 없음");
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
