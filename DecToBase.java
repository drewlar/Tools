//Created by Andrew "Drew" Lara
//Saturday 14 October 2023
import java.math.BigInteger;
import java.util.ArrayList;

public class DecToBase{
    public static void main(String[] args){

        //initalizing variables, starting number, array to hold digits for final number and extra digits after 9 

        String base = args[1];
        BigInteger decNum = new BigInteger(args[0]);
        ArrayList<BigInteger> BIarray = new ArrayList<>();
        char[] listLetters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

        //repeated division to get digits in base 36
        while(!(decNum.compareTo(new BigInteger(base))<0)){
            BIarray.add(decNum.divideAndRemainder(new BigInteger(base))[1]);
            decNum = decNum.divideAndRemainder(new BigInteger(base))[0];
        }
        //add final digit
        BIarray.add(decNum);
        BigInteger bigInteger = new BigInteger("0");

        //print out each digit or symbol (if digit value is over 9), NOTE: Array holds digit values reversed as a result of the division method
        for (int i = BIarray.size() -1; i>=0; i--) {
            bigInteger = BIarray.get(i);
            if(bigInteger.intValue()>=10){
                System.out.print(listLetters[bigInteger.intValue()-10]);
            }else{
            System.out.print(bigInteger.toString());
            }
        }
    }
}