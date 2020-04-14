
<template>

	<div class="student-page-container">
		<md-app>
			<md-app-toolbar class="md-primary">
				<span class="md-title">Sustainable Courses</span>
			</md-app-toolbar>

			<md-app-drawer md-permanent="full">
				<md-toolbar class="md-transparent" md-elevation="0">
					Filter 
				</md-toolbar>

				<md-list>

					<md-list-item>
						<form><input placeholder="Search by Name">

						</form>
					</md-list-item>

					<md-list-item>
				<md-menu  md-direction="bottom-end">
					<md-button md-menu-trigger>SDGs</md-button>
					<md-menu-content>
						<p>SDGS</p>
						<div class="row">
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
							<div class="sdg">
								<img src ="../assets/sdgs/sdg1.jpg">
							</div>
						</div>

					</md-menu-content>

				</md-menu >
					</md-list-item>
					<md-list-item>

					<md-menu  md-direction="right">
						<md-button md-menu-trigger>Sort</md-button>
						<md-menu-content>
							<md-menu-item>Subject</md-menu-item>
							<md-menu-item>Term</md-menu-item>
							<md-menu-item>Minor</md-menu-item>
						</md-menu-content>

					</md-menu >
					</md-list-item>
			</md-list>
		</md-app-drawer>

		<md-app-content>

			<div v-for="c in courses" :key="c">
				<Course :title="c.title" :course="c.course" :CRN="c.CRN" :description="c.description" />
			</div>
			<div v-for="c in courses" :key="c">
				<Course :title="c.title" :course="c.course" :CRN="c.CRN" :description="c.description" />
			</div>
			<div v-for="c in courses" :key="c">
				<Course :title="c.title" :course="c.course" :CRN="c.CRN" :description="c.description" />
			</div>
			<div v-for="c in courses" :key="c">
				<Course :title="c.title" :course="c.course" :CRN="c.CRN" :description="c.description" />
			</div>
		</md-app-content>
	</md-app>
</div>

</template>


<script>
import Course from '@/components/Course.vue'
import course_list from '@/assets/courses.json'
export default {
	name: "Sustainable",
	components: {
		Course,
	},
	data: function () {
		return {
			courses: course_list,
		}
	}
};


</script>

<style scoped>
h3 {
	margin: 40px 0 0;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}

intro{

}
/* Three image containers (use 25% for four, and 50% for two, etc) */
.sdg {
	float: left;
	width: 33.33%;
	padding: 5px;
}

/* Clear floats after image containers */
.row::after {
	content: "";
	clear: both;
	display: table;
}

.md-app {
	max-height: 400px;
	border: 1px solid rgba(#000, .12);
}

.md-drawer {
	width: 230px;
	max-width: calc(100vw - 125px);
}

</style>
