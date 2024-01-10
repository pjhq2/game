import 'package:frontend/models/weapon_model.dart';

class CharacterModel {
  final int STR;
  final int DEX;
  final int INT;
  final int CON;
  final int LUK;
  final int addiSTR;
  final int addiDEX;
  final int addiINT;
  final int addiCON;
  final int addiLUK;
  final int finalSTR;
  final int finalDEX;
  final int finalINT;
  final int finalCON;
  final int finalLUK;
  final String name;
  final int level;
  final String career;
  final int HP;
  final int MP;
  final int power;
  final int defence;
  final int hit;
  final double avoid;
  final double fatal;
  final double fatalAmp;
  final double tolerance;
  final int recovery;
  final int speed;
  final int addiHP;
  final int addiMP;
  final int addiPower;
  final int addiDefence;
  final int addiHit;
  final double addiAvoid;
  final double addiFatal;
  final double addiFatalAmp;
  final double addiTolerance;
  final int addiRecovery;
  final int addiSpeed;
  final int finalHP;
  final int finalMP;
  final int finalPower;
  final int finalDefence;
  final int finalHit;
  final double finalAvoid;
  final double finalFatal;
  final double finalFatalAmp;
  final double finalTolerance;
  final int finalRecovery;
  final int finalSpeed;
  final int EXP;
  final int requiredEXP;
  final int coin;
  final inventory;
  final weapon;
  final helmet;
  final armor;
  final gloves;
  final shoes;
  final core;
  final List<dynamic> skillList;

  CharacterModel({
    required this.STR,
    required this.DEX,
    required this.INT,
    required this.CON,
    required this.LUK,
    required this.addiSTR,
    required this.addiDEX,
    required this.addiINT,
    required this.addiCON,
    required this.addiLUK,
    required this.finalSTR,
    required this.finalDEX,
    required this.finalINT,
    required this.finalCON,
    required this.finalLUK,
    required this.name,
    required this.level,
    required this.career,
    required this.HP,
    required this.MP,
    required this.power,
    required this.defence,
    required this.hit,
    required this.avoid,
    required this.fatal,
    required this.fatalAmp,
    required this.tolerance,
    required this.recovery,
    required this.speed,
    required this.addiHP,
    required this.addiMP,
    required this.addiPower,
    required this.addiDefence,
    required this.addiHit,
    required this.addiAvoid,
    required this.addiFatal,
    required this.addiFatalAmp,
    required this.addiTolerance,
    required this.addiRecovery,
    required this.addiSpeed,
    required this.finalHP,
    required this.finalMP,
    required this.finalPower,
    required this.finalDefence,
    required this.finalHit,
    required this.finalAvoid,
    required this.finalFatal,
    required this.finalFatalAmp,
    required this.finalTolerance,
    required this.finalRecovery,
    required this.finalSpeed,
    required this.EXP,
    required this.requiredEXP,
    required this.coin,
    required this.inventory,
    required this.weapon,
    required this.helmet,
    required this.armor,
    required this.gloves,
    required this.shoes,
    required this.core,
    required this.skillList,
  });

  factory CharacterModel.fromJson(Map<String, dynamic> json) {
    return CharacterModel(
      STR: json['STR'],
      DEX: json['DEX'],
      INT: json['INT'],
      CON: json['CON'],
      LUK: json['LUK'],
      addiSTR: json['추가STR'],
      addiDEX: json['추가DEX'],
      addiINT: json['추가INT'],
      addiCON: json['추가CON'],
      addiLUK: json['추가LUK'],
      finalSTR: json['최종STR'],
      finalDEX: json['최종DEX'],
      finalINT: json['최종INT'],
      finalCON: json['최종CON'],
      finalLUK: json['최종LUK'],
      name: json['이름'],
      level: json['레벨'],
      career: json['직업'],
      HP: json['HP'],
      MP: json['MP'],
      power: json['공격력'],
      defence: json['방어력'],
      hit: json['명중'],
      avoid: json['회피'],
      fatal: json['치명타'],
      fatalAmp: json['치명타증폭'],
      tolerance: json['내성'],
      recovery: json['회복'],
      speed: json['속도'],
      addiHP: json['추가HP'],
      addiMP: json['추가MP'],
      addiPower: json['추가공격력'],
      addiDefence: json['추가방어력'],
      addiHit: json['추가명중'],
      addiAvoid: json['추가회피'],
      addiFatal: json['추가치명타'],
      addiFatalAmp: json['추가치명타증폭'],
      addiTolerance: json['추가내성'],
      addiRecovery: json['추가회복'],
      addiSpeed: json['추가속도'],
      finalHP: json['최종HP'],
      finalMP: json['최종MP'],
      finalPower: json['최종공격력'],
      finalDefence: json['최종방어력'],
      finalHit: json['최종명중'],
      finalAvoid: json['최종회피'],
      finalFatal: json['최종치명타'],
      finalFatalAmp: json['최종치명타증폭'],
      finalTolerance: json['최종내성'],
      finalRecovery: json['최종회복'],
      finalSpeed: json['최종속도'],
      EXP: json['경험치'],
      requiredEXP: json['필요경험치'],
      coin: json['코인'],
      inventory: json['인벤토리'] != null ? Map<String, int>.from(json['인벤토리']) : null,
      weapon: json['무기'] != null ? Map<String, dynamic>.from(json['무기']) : null,
      helmet: json['모자'] != null ? Map<String, dynamic>.from(json['모자']) : null,
      armor: json['갑옷'] != null ? Map<String, dynamic>.from(json['갑옷']) : null,
      gloves: json['장갑'] != null ? Map<String, dynamic>.from(json['장갑']) : null,
      shoes: json['신발'] != null ? Map<String, dynamic>.from(json['신발']) : null,
      core: json['코어'] != null ? Map<String, dynamic>.from(json['코어']) : null,
      skillList: json['스킬리스트'] as List<dynamic>,
    );
  }
}