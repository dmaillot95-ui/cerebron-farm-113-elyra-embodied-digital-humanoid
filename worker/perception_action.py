import json,math,pathlib
# ELYRA reduced perception-action loop. Protocol experiment, not humanoid physics.
world={"target_x":2.0,"obstacle":[0.9,1.1],"dt":0.25}
state={"x":0.0,"energy":100.0,"step":0,"observations":[],"actions":[]}
while state["step"]<20 and abs(world["target_x"]-state["x"])>0.05:
 d=world["target_x"]-state["x"]; obstacle=world["obstacle"][0]<=state["x"]+0.25<=world["obstacle"][1]
 obs={"distance":round(d,3),"obstacle_ahead":obstacle,"energy":round(state["energy"],3)};state["observations"].append(obs)
 if obstacle: action={"type":"sidestep","dx":0.15,"cost":0.25}
 else: action={"type":"walk","dx":min(0.25,max(0,d)),"cost":0.2}
 state["actions"].append(action);state["x"]=round(state["x"]+action["dx"],3);state["energy"]=round(state["energy"]-action["cost"],3);state["step"]+=1
checks={"target_reached":abs(world["target_x"]-state["x"])<=0.05,"energy_valid":0<=state["energy"]<=100,"obstacle_observed":any(o["obstacle_ahead"] for o in state["observations"]),"action_trace":len(state["actions"])==state["step"]}
out={"farm":113,"identity":"ELYRA","experiment":"PERCEPTION_ACTION_LOOP_V1","status":"PASS" if all(checks.values()) else "FAIL","world":world,"final_state":state,"checks":checks,"interfaces":{"cognition":"F112/AELYS","head":"F111","worlds":"F90,F101-F110"},"epistemic":"REDUCED_PROTOCOL_WORLD_NOT_PHYSICS_NOT_AUTONOMOUS_CONSCIOUS_AGENT_NOT_SIM_TO_REAL"}
pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/perception_action.json").write_text(json.dumps(out,indent=2)+"\\n");print(json.dumps(out));raise SystemExit(0 if out["status"]=="PASS" else 1)
