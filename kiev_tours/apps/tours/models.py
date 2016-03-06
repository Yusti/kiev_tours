from django.db import models

class Tour(models.Model):

	# Const values.
	titleMaxLength = 200
	descriptionMaxLength = 4096

	tourWeekendDB = 0
	tourExcursionDB = 1
	tourPersonalGuideDB = 2

	tourWeekendUser = "Tour on weekend"
	tourExcursionUser = "Excursion tour"
	tourPersonalGuideUser = "Personal guide"

	tourChoices = (
		(tourWeekendDB, tourWeekendUser),
		(tourExcursionDB, tourExcursionUser),
		(tourPersonalGuideDB, tourPersonalGuideUser)
		)

# DB fields
	title = models.CharField(max_length = titleMaxLength)
	description = models.CharField(max_length = descriptionMaxLength)
	price = models.IntegerField(default = 0)
	rating = models.IntegerField(default = 0)
	visible = models.BooleanField(default = False)
	tourType = models.IntegerField(choices = tourChoices,
		default = tourExcursionDB)

	def __str__(self):
		return self.title

#TODO: Analyze the logic for main image(more than one, absent image, etc.)
	def getMainImage(self):
		tourImage = TourImage.objects.filter(tour_id=self.pk,
										mainImage=True,	visible = True).first()
		if tourImage != None:
			return tourImage.image
#TODO: Return path to some default picture
		return None

class TourImage(models.Model):
# DB fields
	tour = models.ForeignKey(Tour)
	# TODO: add some constraints to Image size.
	image = models.ImageField(upload_to='img/tours')
	visible = models.BooleanField(default = True)
	mainImage = models.BooleanField(default = False)
