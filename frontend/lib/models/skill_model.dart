class SkillModel {
  final String name;
  final int level;
  final int grade;
  final int damage;
  final String type;
  final int duration;
  final double amp;
  final int maxLevel;

  SkillModel({
    required this.name,
    required this.level,
    required this.grade,
    required this.damage,
    required this.type,
    required this.duration,
    required this.amp,
    required this.maxLevel,
  });

  factory SkillModel.fromJson(Map<String, dynamic> json) {
    return SkillModel(
      name: json['이름'],
      level: json['레벨'],
      grade: json['등급'],
      damage: json['데미지'],
      type: json['유형'],
      duration: json['지속시간'],
      amp: json['증폭'],
      maxLevel: json['최고레벨'],
    );
  }
}