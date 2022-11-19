@i
M = 0
@R2
M = 0
(LOOP)
     @R1 //checks if R1==i
     D = M
     @i
     D = D - M // R1 = R1-i
     @LOOP_END
     D;JEQ
     @R0 //if R0==0 or R1==0
     D = M 
     @R2
     M = M + D
     @i
     M = M + 1
    @LOOP
    0;JMP
(LOOP_END)
@21
0;JMP