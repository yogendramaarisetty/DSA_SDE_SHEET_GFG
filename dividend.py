def divide( dividend: int, divisor: int) -> int:
        c = 0
        sign_val = 1
        if not ((dividend<0 and divisor<0) or (dividend >0 and divisor>0)):
            sign_val = -1
        
        
        dividend,divisor  = abs(dividend),abs(divisor) 
        if abs(dividend)==0 or abs(divisor) ==1:
            if dividend*sign_val >= 2**31:
                return (2**31)-1
            return dividend*sign_val
        
        
        while dividend >= divisor:
            dividend -= divisor
            c+=1
            if c>1000:
                print(dividend,divisor)
                return c
        print(sign_val)
        return sign_val * c

print(divide(2147483647,2))

