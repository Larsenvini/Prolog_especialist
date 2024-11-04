% Base de conhecimento de problemas e sintomas automotivos

% Fatos sobre sintomas
sintoma(bateria_fraca, "A ignição está fraca e as luzes do painel estão apagadas.").
sintoma(falta_de_oleo, "O motor está superaquecendo.").
sintoma(disco_freio_desgastado, "Há um ruído ao frear.").
sintoma(perda_de_potencia, "O carro não acelera como deveria.").
sintoma(falha_de_ignicao, "O motor está falhando ao ligar ou funcionado de maneira irregular.").
sintoma(aquecimento_motor, "O indicador de temperatura está no vermelho.").
sintoma(ruido_motor, "Há um ruído estranho vindo do motor.").

% Regras para diagnosticar problemas baseados em sintomas
diagnostico(bateria_fraca) :- sintoma(bateria_fraca, _).
diagnostico(falta_de_oleo) :- sintoma(falta_de_oleo, _).
diagnostico(disco_freio_desgastado) :- sintoma(disco_freio_desgastado, _).
diagnostico(perda_de_potencia) :- sintoma(perda_de_potencia, _).
diagnostico(falha_de_ignicao) :- sintoma(falha_de_ignicao, _).
diagnostico(aquecimento_motor) :- sintoma(aquecimento_motor, _).
diagnostico(ruido_motor) :- sintoma(ruido_motor, _).

% Regras de inferência de causas prováveis
causa_probavel(bateria_fraca, "A bateria pode estar descarregada ou com problemas.").
causa_probavel(falta_de_oleo, "O nível de óleo pode estar baixo ou o óleo pode estar contaminado.").
causa_probavel(disco_freio_desgastado, "Os discos de freio podem estar gastos e precisam ser substituídos.").
causa_probavel(perda_de_potencia, "Pode haver um problema no sistema de combustível ou uma falha na ignição.").
causa_probavel(falha_de_ignicao, "As velas de ignição podem estar sujas ou danificadas.").
causa_probavel(aquecimento_motor, "Pode haver uma falha no sistema de arrefecimento ou falta de líquido refrigerante.").
causa_probavel(ruido_motor, "Pode ser um problema mecânico interno, como um rolamento danificado.").

% Regra para diagnosticar uma causa
diagnostico_causa(Sintoma, Problema, Causa) :-
    diagnostico(Problema),
    sintoma(Problema, Sintoma),
    causa_probavel(Problema, Causa).
