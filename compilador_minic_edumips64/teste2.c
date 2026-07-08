/* Autor: Josival Salvador Monteiro Junior */
/* Teste com o codigo C exatamente como esta no enunciado do Trabalho 09,
   sem nenhuma adaptacao -- inclui 'void' em process_data e 'main(void)'.
   A gramatica MiniC.g4 ja aceita VOID como sinonimo de "sem retorno" e
   de "lista de parametros vazia" (linhas 53 e 67), entao este arquivo
   deve compilar sem qualquer ajuste.

   Calculo esperado (resultado final impresso):
     local_sum = 10+20+30+5+8 = 73
     73 >= 100? nao -> else: global_counter = 0 - 1 = -1
     while (global_counter < 5): soma +2 repetidamente
       -1 -> 1 -> 3 -> 5  (para quando chega em 5, pois 5 < 5 e falso)
     resultado esperado: 5
*/

int global_counter = 0;

void process_data(int a, int b, int c, int d, int e) {
  int local_sum = a + b + c + d + e;
  if (local_sum >= 100) {
    global_counter = global_counter + 1;
  } else {
    global_counter = global_counter - 1;
  }
  while (global_counter < 5) {
    global_counter = global_counter + 2;
  }
}

int main(void) {
  process_data(10, 20, 30, 5, 8);
  printf("%d\n", global_counter);
}