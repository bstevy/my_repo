select 
concat(
	substring(c.jour,1, 2),
	case when c.type_cours = "Hip Hop" then "HH"
	when c.type_cours = "Waak/Street jazz" then "WSJ"
	else c.type_cours end,
	"_",
	c.niveau
) as niveau, 
ic.role,
users.firstname,
users.lastname, 
concat(
case
            when cmd.validite = date '2019-07-31' then 'A'
            when cmd.validite = date '2019-03-31' then 'T'
            else ''
        end, 
		case when cmd.id_user2 is null then '' else 'D' end,
		case when cmd.illimite = 1 then 'I' else '' end,
		case when cmd.reduit = 1 then 'R' else '' end
) as abo
FROM `users` inner join inscription_cours ic on users.id = ic.id_user 
inner join cours c on c.id = ic.id_cours 
inner join commande cmd on users.id in (cmd.id_user1, cmd.id_user2)
where ic.validite >= CURRENT_DATE
and 'annule' not in (ic.status, cmd.status)
and cmd.validite >= CURRENT_DATE
and c.id <> 9
order by c.id, ic.role, users.firstName, users.lastname, abo
;