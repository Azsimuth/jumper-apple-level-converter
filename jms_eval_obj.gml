///jms_eval_obj(letter, x, y) -- example jms_eval_obj(B) --> Bricks
var l;
l = argument0;
xx = argument1;
yy = argument2;
  
switch l {
case "B":
instance_create(xx,yy,ObjBrick); break;
case "c":
instance_create(xx,yy,ObjCoin); break;
case "C":
instance_create(xx,yy,ObjBluCoin); break;
case "b":
instance_create(xx,yy,ObjCrate); break;
case "J":
instance_create(xx,yy,ObjJumper); break;
case "F":
instance_create(xx,yy,ObjFlag); break;
case "m":
instance_create(xx,yy,ObjMachineGunner); break;
case "l":
instance_create(xx,yy,obj_lazergunner); break;
case "s":
instance_create(xx,yy,ObjSiren); break;
case "t":
instance_create(xx,yy,obj_attackmite_turret); break;
case "+":
instance_create(xx,yy,ObjHealthKit); break;
case "×":
instance_create(xx,yy,ObjSpikes); break;
}
