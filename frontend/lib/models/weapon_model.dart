class WeaponModel {
  final String id;
  final String name;
  final int grade;
  final String gradeName;
  final int reinLevel;
  final int maxReinLevel;
  final String type;
  final int minDamage;
  final int maxDamage;
  final double amp;
  final int reinMinDamage;
  final int reinMaxDamage;
  final double reinAmp;
  final int finalMinDamage;
  final int finalMaxDamage;
  final double finalAmp;
  // final Map<String, int>? addiAbility;
  // final List<Map<String, dynamic>?> weaponSkillList;

  WeaponModel({
    required this.id,
    required this.name,
    required this.grade,
    required this.gradeName,
    required this.reinLevel,
    required this.maxReinLevel,
    required this.type,
    required this.minDamage,
    required this.maxDamage,
    required this.amp,
    required this.reinMinDamage,
    required this.reinMaxDamage,
    required this.reinAmp,
    required this.finalMinDamage,
    required this.finalMaxDamage,
    required this.finalAmp,
    // required this.addiAbility,
    // required this.weaponSkillList,
  });

  factory WeaponModel.fromJson(Map<String, dynamic> json) {
    // print(json['추가능력치']);
    // print(json['무기스킬리스트']);
    return WeaponModel(
      id: json['id'],
      name: json['이름'],
      grade: json['등급'],
      gradeName: json['등급이름'],
      reinLevel: json['강화레벨'],
      maxReinLevel: json['최고강화레벨'],
      type: json['유형'],
      minDamage: json['최소데미지'],
      maxDamage: json['최대데미지'],
      amp: json['증폭'],
      reinMinDamage: json['강화최소데미지'],
      reinMaxDamage: json['강화최대데미지'],
      reinAmp: json['강화증폭'],
      finalMinDamage: json['최종최소데미지'],
      finalMaxDamage: json['최종최대데미지'],
      finalAmp: json['최종증폭'],
      // addiAbility: json['추가능력치'] != null ? Map<String, int>.from(json['addiAbility']) : null,
      // weaponSkillList: json['무기스킬리스트'] as List<Map<String, dynamic>?>,
    );
  }
}