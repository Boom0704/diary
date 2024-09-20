<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.sql.Connection"%>   
<%@page import="java.sql.DriverManager"%>   
<%@page import="java.sql.PreparedStatement"%>   
<%@page import="java.sql.ResultSet"%>   
<%@page import="java.sql.SQLException"%>   

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- ArrayList 선언 -->
	<%! ArrayList<String> list = new ArrayList<>(); %>
	
	<%
		// db와 연결
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			// 1. 드라이버 로딩
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("드라이버 등록 성공");

			// 2. DB 연결
			String url = "jdbc:oracle:thin:@127.0.0.1:1521:xe";
			String db_id = "java";
			String db_pw = "oracle";
			conn = DriverManager.getConnection(url, db_id, db_pw);
			System.out.println("접속 성공");
			
			// 3. SQL 쿼리 작성 및 실행
			StringBuffer query = new StringBuffer();
			query.append(" SELECT info_no");
			query.append("      , nm");
			query.append("      , email");
			query.append("      , hobby");
			query.append(" FROM tb_info");
			query.append(" WHERE nm LIKE  ? || '%' ");
			System.out.println(query);
			
			ps = conn.prepareStatement(query.toString());
			ps.setString(1, "김"); // 이름이 '김'으로 시작하는 데이터 검색
			rs = ps.executeQuery(); // 쿼리 실행
			
			// 4. 결과 처리 및 ArrayList에 데이터 추가
			while(rs.next()) {
				int no = rs.getInt("info_no");
				String nm = rs.getString("nm");
				String email = rs.getString("email");
				String hobby = rs.getString("hobby");
				
				System.out.println("no: " + no + ", nm: " + nm 
						          + ", email: " + email + ", hobby: " + hobby);
				
				// 데이터를 ArrayList에 추가
				list.add(nm); // 이름만 추가
			}
		} catch (ClassNotFoundException e) {
			System.out.println("드라이버 등록 실패");
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			// 리소스 해제
			if(rs != null) { try { rs.close(); } catch (SQLException e) { e.printStackTrace(); } }
			if(ps != null) { try { ps.close(); } catch (SQLException e) { e.printStackTrace(); } }
			if(conn != null) { try { conn.close(); } catch (SQLException e) { e.printStackTrace(); } }
		}
	%>

	<h1>학생 목록</h1>
	<ul>
		<% 
		// ArrayList에서 데이터 출력
		for (String name : list) { 
		%>
			<li>이름: <%= name %></li>
		<% 
		} 
		%>
	</ul>
</body>
</html>
