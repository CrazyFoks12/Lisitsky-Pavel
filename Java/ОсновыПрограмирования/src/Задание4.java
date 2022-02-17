import java.util.Scanner;
public class Задание4 
{
	public static void main(String[] args) {
		final String login="Admin", password="Admin", user="Павел";
		String u_login, u_password;
		Scanner input = new Scanner(System.in);
		System.out.println("Введите логин: ");
			u_login = input.nextLine();
		System.out.println("Введите пароль: ");
			u_password = input.nextLine();
	if(u_login.equals(login) && u_password.equals(password))
		System.out.println("Добро пожаловать " + user);
	else
		System.out.println("Вход запрещён");
	}
}