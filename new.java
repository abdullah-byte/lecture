import java.util.Scanner;

public static void public static void main(String[] args) {
  int a = (int)(Math.random() * 10);
  int b = (int)(Math.random() * 10));

  Scanner input = new Scanner(System.in);
  System.out.print("What is " + a + " + " + b + " ?");
  int answer = input.nextInt();

  while(a + b != answer){
    System.out.print("wrong answer, try again. What is " + a + "+" + b + "?");
    answer = input,nextInt();

  }
  System.out.println("you got it ");
}
