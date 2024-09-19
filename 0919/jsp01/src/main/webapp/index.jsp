<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.Date" %>
<%@ page import="java.text.SimpleDateFormat" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- 선언부 -->
	<%! public int multiply(int x, int y){
		return x * y;
	} %>
	<!-- 선언부 -->
	
	<!-- 자바블록 -->
	<%
	 Date today = new Date();
	 SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
	 String dateStr = format.format(today);
	 int result = multiply(2, 10);
	%>
	<!-- 자바블록 -->
	<h1> Hello </h1>
	<h1> 오늘의 날짜는 : <%=dateStr%></h1>
	<h1> 2 * 10 = <%=result%></h1>

</body>
</html>