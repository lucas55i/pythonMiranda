# Criação das Regras de Negocio para o cliente Phoenix

## _O Cliente Phoenix Só terá ITSM e Notificações, nesse primeiro momento_

Para facilitar a organização e criação das RNs(Regras de Negócios) vou separar todas em ativdades em 3 categorias, cada uma com suas respectivas ações.


| Problem                     | Reincidência          | Resolved              |
| --------------------------- | --------------------- | --------------------- |
| Acertar as conditions       | Acertar as conditions | Acertar as conditions |
| Chamado aberto corretamente | Comentar no chamado   | Encerrar o chamado    |
| Notificações                | Notificações          | Notificações          |

### Observações

<p> A wit só atuará em alarmes com prioridade igual ou superior a 3.</p>

Todo alarma chegará com duas Tags `CERVELLO_SOLICITANTE` e `CERVELLO_FAVORECIDO` essas tags devém ser passadas em cada abertura de chamado.

Ambas as informações que se devem passar para abrir o chamdo estão na planilha Trigger do grupo Phoenix, que se encontra no sharesPoint

Foi enviado um PDF contendo os procedimentos para abertura de chamado no cliente


#### Exceções
Á exceções de trigger que fogem ás regras.

    * Quando cair em exceções deve-se acionar alguns análistas a aparte
    * Deve-se incluir o análista na notifiação de SMPT para esse tipo de alarme
    * Geralmente são regras em disco, todas as inforações contam na planilha Trigger do grupo Phoenix


dois novos campos em managers, plans, pipelines,  campos ficam fora de metadata

    * version: 0 # Padrão de versionamento
    * enabled: true

----

### Nomenclatura

Pipelines

*Substituir o `traço` por `underline`*

- Nome Problem: new_problem_zabbix_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux || new_problem_zabbix_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}` _windows
- Nome Reincidência: repeated_problem_zabbix_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux || repeated_problem_zabbix_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_windows
- Nome Resolved: problem_resolved_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux || problem_resolved_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_windows


Plans - Ações
    
- Nome Abertura: itsm_open_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux |----| itsm_open_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_windows
- Nome Reincidência : itsm_reopen_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux |----| itsm_reopen_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_windows
- Nome Comentario / Resolved: itsm_resolved_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_linux |----| itsm_resolved_ticket_to_`{{ Regra na WIT }}`-`{{ Tipo de Alarme }}`_windows

Plans - Notificações
- Notificações Abertura: add_comment_to_zabbix+notify_new_problem_chats+emails_no_automation
- Nome Comentario: add_comment_to_zabbix+notify_repeated_problem_chats+emails_no_automacao
- Nome Resolved: notify_problem_resolved_chats+emails