<? php

?>

<!DOCTYPE html>
<html lang="pt-br">
   <head>
       <meta charset="utf-8">
       <title>Teste Boot</title>
   </head>
   <body>	
   
       <form method="POST" action="boot_test.php">
           Valor: <input type="text"name="valor" placeholder="R$ 300" required><br><br>
           Moeda: <input type="text" name="moeda"  placeholder="EURUSD" required><br><br>
           Operação: <input type="text" name="operacao" placeholder="CALL OU PUT"required><br><br>
           Hora: <input type="text" name="hora" placeholder="10:22:58" required><br><br>
           <br>
           <br>
           <input type="submit" value="Enviar">
       </form>
   </body>