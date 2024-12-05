from django.db import models
from core.libs.models import TimeStampModel
from django_ckeditor_5.fields import CKEditor5Field


class Company(TimeStampModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="images/company_logos/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Job(TimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = CKEditor5Field(config_name="extends")
    job_location = models.CharField(max_length=255)
    min_salary = models.DecimalField(
        "Minimum Annual Salary USD", max_digits=10, decimal_places=2
    )
    max_salary = models.DecimalField(
        "Maximum Annual Salary USD", max_digits=10, decimal_places=2
    )
    job_type = models.CharField(
        max_length=255,
        choices=[
            ("Full Time", "Full Time"),
            ("Part Time", "Part Time"),
            ("Contract", "Contract"),
            ("Internship", "Internship"),
            ("Temporary", "Temporary"),
        ],
    )
    # salary_distribution_period = models.CharField(
    #     max_length=255,
    #     choices=[
    #         ("Weekly", "Weekly"),
    #         ("Monthly", "Monthly"),
    #         ("Half Yearly", "Half Yearly"),
    #         ("Yearly", "Yearly"),
    #     ],
    # )
    expiry_date = models.DateField()
    job_level = models.CharField(
        max_length=255,
        choices=[
            ("Entry Level", "Entry Level"),
            ("Mid Level", "Mid Level"),
            ("Expert Level", "Expert Level"),
        ],
    )
    required_experience = models.CharField(
        max_length=255,
        choices=[
            ("No Experience", "No Experience"),
            ("1 Year", "1 Year"),
            ("2 Years", "2 Years"),
            ("3 Years", "3 Years"),
            ("4 Years", "4 Years"),
            ("5 Years", "5 Years"),
            ("6 Years", "6 Years"),
            ("7 Years", "7 Years"),
            ("8 Years", "8 Years"),
            ("9 Years", "9 Years"),
            ("10 Years", "10 Years"),
            ("10+ Years", "10+ Years"),
        ],
    )
    required_education = models.CharField(
        max_length=255,
        choices=[
            ("High School", "High School"),
            ("Diploma", "Diploma"),
            ("Bachelor", "Bachelor"),
            ("Master", "Master"),
            ("PhD", "PhD"),
        ],
    )

    def __str__(self):
        return self.title

class Application(TimeStampModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cv = models.FileField(upload_to="files/applicants_cv/")

    def __str__(self):
        return f"{self.job.title}"
