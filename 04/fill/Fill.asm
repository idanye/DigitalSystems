@i // i = 0
M = 0
@KBD // EndScreen = KDB - 1 - screen 
D = A - 1
@SCREEN 
D = D - A 
@END_SCREEN
M = D + 1
(LOOP)
     @END_SCREEN // if (endscreen - i == 0)
     D = M
     @i
     D = D - M
    @LOOP_END // if (D == 0)
    D;JEQ
     @KBD
     D = M
     @WHITE
     D;JEQ
     @BLACK
     D;JNE
    (CONT_LOOP)
     @i
     M = M + 1 // i++
    @LOOP
    0;JMP
(LOOP_END)
(BLACK)
     @i 
     D = M
     @SCREEN // A = Screen + i
     D = A + D 
     @temp
     M = D
     @temp
     A = M
     M = -1 // M[A] = -1
     @CONT_LOOP
     0;JMP
(WHITE)
     @i 
     D = M
     @SCREEN // A = Screen + i
     A = A + D
     @temp
     M = D
     @temp
     A = M
     M = 0 // M[A] = 0
     @CONT_LOOP
     0;JMP
(END)
     @END
     0;JMP