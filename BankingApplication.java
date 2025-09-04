import java.util.*;

public class BankingApplication {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name:");
        String name = sc.nextLine();
        System.out.println("Enter your ID:");
        String id = sc.nextLine();

        BankAccount obj1 = new BankAccount(name, id);
        obj1.showMenu();
        sc.close();
    }
}

class BankAccount {
    int balance;
    int previousTransaction;
    String customerName;
    String customerId;

    BankAccount(String cname, String cid) {
        customerName = cname;
        customerId = cid;
    }

    void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
            previousTransaction = amount;
        } else {
            System.out.println("Invalid deposit amount. Please enter a positive amount.");
        }
    }

    void withdraw(int amount) {
        if (amount > balance) {
            System.out.println("Insufficient balance! You cannot withdraw more than your available balance.");
        } else if (amount > 0) {
            balance -= amount;
            previousTransaction = -amount;
        } else {
            System.out.println("Invalid withdrawal amount. Please enter a positive amount.");
        }
    }

    void getPreviousTransaction() {
        if (previousTransaction > 0) {
            System.out.println("Deposited: " + previousTransaction);
        } else if (previousTransaction < 0) {
            System.out.println("Withdrawn: " + Math.abs(previousTransaction));
        } else {
            System.out.println("No transaction occurred");
        }
    }

    void showMenu() {
        char option;
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome " + customerName);
        System.out.println("Your ID is " + customerId);
        System.out.println("\n");
        System.out.println("A. Check Balance");
        System.out.println("B. Deposit");
        System.out.println("C. Withdraw");
        System.out.println("D. Previous Transaction");
        System.out.println("E. Exit");

        do {
            System.out.println("================");
            System.out.println("Enter an option");
            System.out.println("=================");
            option = sc.next().charAt(0);
            System.out.println("\n");

            switch (option) {
                case 'A':
                    System.out.println("---------------");
                    System.out.println("Balance = " + balance);
                    System.out.println("---------------");
                    break;

                case 'B':
                    System.out.println("---------------");
                    System.out.println("Enter an amount to deposit:");
                    System.out.println("---------------");
                    int depositAmount = sc.nextInt();
                    deposit(depositAmount);
                    break;

                case 'C':
                    System.out.println("---------------");
                    System.out.println("Enter an amount to withdraw:");
                    System.out.println("---------------");
                    int withdrawAmount = sc.nextInt();
                    withdraw(withdrawAmount);
                    break;

                case 'D':
                    System.out.println("---------------");
                    getPreviousTransaction();
                    System.out.println("---------------");
                    break;

                case 'E':
                    System.out.println("****************");
                    break;

                default:
                    System.out.println("Invalid option! Please enter again.");
                    break;
            }
        } while (option != 'E');

        System.out.println("Thank you, " + customerName + ", for using our services!");
        sc.close();
    }
}