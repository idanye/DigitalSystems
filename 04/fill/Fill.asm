(START) // initializing i = screen
     @SCREEN
     D = A
     @i // i = screen
     M = D
     @LOOP
     0;JMP

(LOOP)
     @i // if (KBD - i == 0)
     D = M
     @KBD
     D = A - D
     @START
     D;JEQ
     @KBD // if KBD == 0 > run WHITE, otherwise BLACK
     D = M
     @WHITE
     D;JEQ
     @BLACK
     D;JNE
    (CONT_LOOP) // after set the pixel, we will promote i
     @i
     M = M + 1
     @LOOP
     0;JMP

(BLACK)
     @i   
     A = M
     M = -1 // M[A] = -1
     @CONT_LOOP
     0;JMP
     
(WHITE)
     @i
     A = M
     M = 0 // M[A] = 0
     @CONT_LOOP
     0;JMP
