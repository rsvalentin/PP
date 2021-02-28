import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.*;
import java.util.Stack;

public class Calculator extends JFrame {
    JButton digits[] = {
            new JButton(" 0 "),
            new JButton(" 1 "),
            new JButton(" 2 "),
            new JButton(" 3 "),
            new JButton(" 4 "),
            new JButton(" 5 "),
            new JButton(" 6 "),
            new JButton(" 7 "),
            new JButton(" 8 "),
            new JButton(" 9 ")
    };

    JButton operators[] = {
            new JButton(" + "),
            new JButton(" - "),
            new JButton(" * "),
            new JButton(" / "),
            new JButton(" = "),
            new JButton(" ( "),
            new JButton(" ) "),
            new JButton(" C ")
    };

    String oper_values[] = {"+", "-", "*", "/", "=", "(", ")",""};

    char operator;

    JTextArea area = new JTextArea(3, 5);

    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        calculator.setSize(300, 230);
        calculator.setTitle(" Java-Calc, PP Lab1 ");
        calculator.setResizable(true);
        calculator.setVisible(true);
        calculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public Calculator() {
        add(new JScrollPane(area), BorderLayout.NORTH);
        JPanel buttonpanel = new JPanel();
        buttonpanel.setLayout(new FlowLayout());

        for (int i=0;i<10;i++)
            buttonpanel.add(digits[i]);

        for (int i=0;i<8;i++)
            buttonpanel.add(operators[i]);

        add(buttonpanel, BorderLayout.CENTER);
        area.setForeground(Color.BLACK);
        area.setBackground(Color.WHITE);
        area.setLineWrap(true);
        area.setWrapStyleWord(true);
        area.setEditable(false);

        for (int i=0;i<10;i++) {
            int finalI = i;
            digits[i].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent actionEvent) {
                    area.append(Integer.toString(finalI));
                }
            });
        }

        for (int i=0;i<8;i++){
            int finalI = i;
            operators[i].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent actionEvent) {
                    if (finalI == 7)
                        area.setText("");
                    else
                    if (finalI == 4) {
                        String res;
                        try {
                            res = area.getText();
                            res = formaPoloneza(res);
                            Stack<Double> stack = new Stack<>();
                            for (int i = 0; i < res.length(); i++) {
                                char c = res.charAt(i);
                                if (Character.isDigit(c)) {
                                    stack.push((double) (c-'0'));
                                } else {
                                    double nr1 = stack.pop();
                                    double nr2 = stack.pop();
                                    switch (c) {
                                        case '+':
                                            stack.push(nr2 + nr1);
                                            break;
                                        case '-':
                                            stack.push(nr2 - nr1);
                                            break;
                                        case '/':
                                            stack.push(nr2 / nr1);
                                            break;
                                        case '*':
                                            stack.push(nr2 * nr1);
                                            break;
                                    }
                                }
                            }
                            res = Double.toString(stack.pop());
                            area.append(" = " + res);
                        } catch (Exception e) {
                            area.setText(" !!!Probleme!!! ");
                        }
                    }
                    else {
                        area.append(oper_values[finalI]);
                        operator = oper_values[finalI].charAt(0);
                    }
                }
            });
        }
    }

    static int prioritate(char op) {
        int nivel = 0;
        switch (op) {
            case '/':
            case '*':
                nivel = 2;
                break;
            case '+':
            case '-':
                nivel = 1;
                break;
        }
        return nivel;
    }

    static String formaPoloneza(String expr) {
        String res = new String("");
        Stack<Character> stack = new Stack();

        for(int i=0; i<expr.length(); i++) {
            char c = expr.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                res = res + c;
            }
            else if (c == '(') {
                stack.push(c);
            }
            else if (c == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    res = res + stack.pop();
                }
                if (!stack.isEmpty() && stack.peek() != '(') {
                    return "Probleme";
                }
                else {
                    stack.pop();
                }
            }
            else {
                while (!stack.isEmpty() && prioritate(c) <= prioritate(stack.peek())) {
                    if (stack.peek() == '(') {
                        return "Probleme";
                    }
                    res = res + stack.pop();
                }
                stack.push(c);
            }
        }
        while (!stack.isEmpty()) {
            if(stack.peek() == '(') {
                return "Probleme";
            }
            res = res + stack.pop();
        }
        return res;
    }
}