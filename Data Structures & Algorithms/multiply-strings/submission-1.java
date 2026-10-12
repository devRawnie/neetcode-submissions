class Solution {
    public StringBuilder multiply_digits(String num1, int digit){
        StringBuilder sb = new StringBuilder();
        int rem = 0;
        for(int i = num1.length()-1; i >= 0; i--){
            int ndigit = num1.charAt(i) - '0';
            int temp = ndigit * digit + rem;
            rem = (int) temp / 10;
            temp = temp % 10;
            sb.append((char) (temp + '0'));
        }
        if(rem > 0){
            sb.append((char)(rem + '0'));
        }
        return sb.reverse();
    }

    public String add_strings(String num1, String num2){
        int rem = 0;
        int i = 0;
        StringBuilder sb = new StringBuilder();
        while(i < num1.length() && i < num2.length()){
            int d1 = (int) num1.charAt(i) - '0';
            int d2 = (int) num2.charAt(i) - '0';
            int d = d1 + d2 + rem;
            rem = (int) d / 10;
            sb.append((char)(d%10 + '0'));
            i++;
        }
        while(i < num1.length()){
            int d1 = (int) num1.charAt(i) - '0';
            int d = d1 + rem;
            rem = (int) d / 10;
            sb.append((char)(d%10 + '0'));
            i++;
        }
        while(i < num2.length()){
            int d2 = (int) num2.charAt(i) - '0';
            int d = d2 + rem;
            rem = (int) d / 10;
            sb.append((char)(d%10 + '0'));
            i++;
        }

        if (rem > 0){
            sb.append((char)(rem + '0'));
        }
        return sb.toString();
    }
    public String multiply(String num1, String num2) {
        if (num1.charAt(0) == '0') return num1;
        if (num2.charAt(0) == '0') return num2;
        if (num1.length() > num2.length()){
            String temp = num1;
            num1 = num2;
            num2 = temp;
        }
        String[] sarr = new String[num1.length()];
        int zero_count = 0;
        for(int i = num1.length()-1; i>=0; i--){
            int digit = (int) num1.charAt(i) - '0';
            StringBuilder temp = multiply_digits(num2, digit);
            for(int z = 0; z < zero_count; z++){
                temp.append('0');
            }
            zero_count += 1;
            sarr[i] = temp.reverse().toString();
        }
        if(sarr.length == 1){
            return new StringBuilder(sarr[0]).reverse().toString();
        }

        String result = new String();
        for(int i = 1; i < sarr.length; i++){
            if(result.length() == 0){
                result = add_strings(sarr[i], sarr[i-1]);
            }
            else {
                result = add_strings(result, sarr[i]);
            }
        }
        return new StringBuilder(result).reverse().toString();
    }
}
