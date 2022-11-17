@i
M = 0
@R2
M = 0
(LOOP)
     @R1 //checks if R1==i
     D = M
     @i
     D = D-M // R1 = R1-i
     @12
     D;JEQ
    @LOOP_END
    D;JEQ
     @R0 //if R0==0 or R1==0
     D = M
     @R2
     M = D
     @LOOP_END
     D;JEQ
     @R1
     D = M
     @R2
     M = D
     @LOOP_END
     D;JEQ
     @R0 
     D = M
     @R2 // R2=R2+R0
     M = M + D
    @LOOP
    0;JMP
(LOOP_END)
@33
0;JMP