from django.db import models

# Create your models here.
class FirstYearStudent(models.Model):
    hall_ticket_number = models.CharField(max_length = 12, primary_key=True)
    batch_id   = models.IntegerField(default = 0)
    section_id = models.CharField(max_length = 5)
    department = models.CharField(max_length = 5)
    m1_points = models.IntegerField(default = 0)
    m1_grade = models.CharField(max_length = 5)
    applied_physics_points = models.IntegerField(default = 0)
    applied_physics_grade = models.CharField(max_length = 5)
    english_points = models.IntegerField(default = 0)
    english_grade = models.CharField(max_length = 5)
    engineering_graphics_points = models.IntegerField(default = 0)
    engineering_graphics_grade = models.CharField(max_length = 5)
    problem_solving_and_computer_points = models.IntegerField(default = 0)
    problem_solving_and_computer_grade = models.CharField(max_length = 5)
    applied_physics_lab_points = models.IntegerField(default = 0)
    applied_physics_lab_grade = models.CharField(max_length = 5)
    problem_solving_and_computer_prog_points = models.IntegerField(default = 0)
    problem_solving_and_computer_prog_grade = models.CharField(max_length = 5)
    inFormation_technology_workshop_points = models.IntegerField(default = 0)
    inFormation_technology_workshop_grade = models.CharField(max_length = 5)

    class Meta:
        db_table = 'firstyearsemester1_1718'

class SecondYearStudent(models.Model):
    hall_ticket_number = models.CharField(max_length = 12, primary_key=True)
    batch_id = models.IntegerField(default = 0)
    section_id = models.CharField(max_length = 5)
    department = models.CharField(max_length = 5)
    coa_points = models.IntegerField(default = 0)
    coa_grade = models.CharField(max_length = 5)
    dbms_points = models.IntegerField(default = 0)
    dbms_grade = models.CharField(max_length = 5)
    dbmslab_points = models.IntegerField(default = 0)
    dbmslab_grade = models.CharField(max_length = 5)
    dld_mp_points = models.IntegerField(default = 0)
    dld_mp_grade = models.CharField(max_length = 5)
    dldmplab_points = models.IntegerField(default = 0)
    dldmplab_grade = models.CharField(max_length = 5)
    es_points = models.IntegerField(default = 0)
    es_grade = models.CharField(max_length = 5)
    mfcs_points = models.IntegerField(default = 0)
    mfcs_grade = models.CharField(max_length = 5)
    oopjava_points = models.IntegerField(default = 0)
    oopjava_grade = models.CharField(max_length = 5)
    oopjavalab_points = models.IntegerField(default = 0)
    oopjavalab_grade = models.CharField(max_length = 5)
    
    class Meta:
        db_table = 'secondyearsemester1_1718'

class ThirdYearStudent(models.Model):
    hall_ticket_number = models.CharField(max_length = 12, primary_key=True)
    batch_id = models.IntegerField(default = 0)
    section_id = models.CharField(max_length = 5)
    department = models.CharField(max_length = 5)
    adbms_points = models.IntegerField(default = 0)
    adbms_grade = models.CharField(max_length = 5)
    cd_points = models.IntegerField(default = 0)
    cd_grade = models.CharField(max_length = 5)
    cncdlab_points = models.IntegerField(default = 0)
    cncdlab_grade = models.CharField(max_length = 5)
    dccn_points = models.IntegerField(default = 0)
    dccn_grade = models.CharField(max_length = 5)
    dm_points = models.IntegerField(default = 0)
    dm_grade = models.CharField(max_length = 5)
    dmlab_points = models.IntegerField(default = 0)
    dmlab_grade = models.CharField(max_length = 5)
    dwdm_points = models.IntegerField(default = 0)
    dwdm_grade = models.CharField(max_length = 5)
    hpve_points = models.IntegerField(default = 0)
    hpve_grade = models.CharField(max_length = 5)
    ipr_points = models.IntegerField(default = 0)
    ipr_grade = models.CharField(max_length = 5)
    ooad_points = models.IntegerField(default = 0)
    ooad_grade = models.CharField(max_length = 5)
    se_points = models.IntegerField(default = 0)
    se_grade = models.CharField(max_length = 5)
    
    class Meta:
        db_table = 'thirdyearsemester1_1718'