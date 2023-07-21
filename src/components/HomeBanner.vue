<!-- eslint-disable prettier/prettier -->
<template>
  <Loading v-if="loading" />
  <section class="section how-it-works">
    <div class="container">
      <div :class="['row', roundClass, typeClass]">
        <div class="col-12 col-md-8 col-lg-8 offset-md-2">
          <div class="section-header text-center">
            <h2 ref="refTop">
              {{ roundTitle }} <a v-if="isStart">{{ keyIndex }}/{{ roundCount }}</a>
            </h2>
            <p v-if="!isStart" v-html="roundSubTitle"></p>
          </div>
        </div>
        <div
          class="col-12 col-md-8 col-lg-8 offset-lg-2 offset-md-2 mb-2"
          v-for="score in scores"
          :key="score.id"
        >
          <div class="progress-bar-custom">
            <div class="pro-progress">
              <div
                :class="['tooltip-toggle', score.score_class]"
                tabindex="{{ score.id }}"
                :style="{ width: score.score_percent }"
              ></div>
              <div :class="['tooltip', score.score_class]" :style="{ left: score.score_percent }">
                {{ score.score }}
              </div>
            </div>
            <h6 class="mt-1">{{ score.object + " : " + score.prompt }}</h6>
          </div>
        </div>
      </div>

      <div class="row" v-if="showMark">
        <div class="col-12 col-md-8 col-lg-8 offset-lg-2 offset-md-2 mb-2">
          <div class="progress-bar-custom">
            <h6 class="mt-1">Less Creative (1 ~ 1.6)</h6>
            <div class="pro-progress">
              <div class="tooltip-toggle low-score" style="width: 26%"></div>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-8 col-lg-8 offset-lg-2 offset-md-2 mb-2">
          <div class="progress-bar-custom">
            <h6 class="mt-1">More Creative (1.7 ~ 3.3)</h6>
            <div class="pro-progress">
              <div class="tooltip-toggle middle-score" style="width: 50%"></div>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-8 col-lg-8 offset-lg-2 offset-md-2 mb-2">
          <div class="progress-bar-custom">
            <h6 class="mt-1">Very Creative (3.4 ~ 5)</h6>
            <div class="pro-progress">
              <div class="tooltip-toggle high-score" style="width: 70%"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="row" v-if="!searchHide">
        <div class="search-box col-md-12 col-lg-12" ref="refDiv" v-if="!loading">
          <form>
            <div class="form-group search-location">
              <input
                type="text"
                class="form-control"
                placeholder=""
                disabled
                v-model="inputString"
              />
            </div>
            <div class="form-group search-info">
              <input
                type="text"
                class="form-control"
                :placeholder="'Enter creative use for ' + inputString"
                v-model="ideaText"
                @keyup.enter="sendIdea"
              />
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-12 col-md-8 col-lg-8 offset-lg-2 offset-md-2 mb-4">
          <button
            class="btn btn-primary login-btn w-25 mx-auto"
            type="button"
            v-if="!btnHide"
            @click="btnClick"
          >
            {{ btnTitle }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import ideaService from "../services/ideaService"
import authService from "../services/authService"
import { excelParser } from "../services/excel-parser"
import Loading from "../components/Loading.vue"
export default {
  name: "HomeBanner",
  props: {
    msg: String
  },
  components: {
    Loading
  },
  data() {
    return {
      ideaText: "",
      inputString: "",
      round: 1,
      roundTitle: "Practice",
      roundSubTitle: "",
      roundClass: "practice",
      roundCount: 3,
      step: 1,
      wordIndex: 0,
      keyIndex: 0,
      username: "",
      scores: [],
      loading: true,
      btnTitle: "Start",
      typeClass: "test-type",
      isFinished: false,
      isResult: false,
      isStart: false,
      isFinal: false,
      btnHide: false,
      searchHide: false,
      showMark: false
    }
  },
  async mounted() {
    await this.getExamInformation()
    this.loading = false
  },
  beforeCreate() {
    this.loading = true
    authService.checkUserSession().catch((err) => {
      this.loginError = err.response.data
    })
  },
  computed: {},
  methods: {
    async sendIdea() {
      this.loginError = ""
      if (this.inputString == "" || this.ideaText == "") {
        console.log("135")
      } else {
        let score = 0
        this.loading = true
        const scoreData = await ideaService.getIdeaScore({
          inputString: this.inputString,
          ideaText: this.ideaText
        })
        if (scoreData) {
          score = scoreData.originality
        }
        await ideaService.checkIdeaScore({
          inputString: this.inputString,
          ideaText: this.ideaText,
          round: this.round,
          score: score
        })
        this.loading = false
        this.getExamInformation()
      }
    },
    async getExamInformation() {
      const roundInfo = await ideaService.checkRoundInfo()
      if (roundInfo) {
        this.scores = roundInfo.idea_list
        this.round = roundInfo.round
        this.wordIndex = roundInfo.object_index
        switch (this.round) {
          case 1:
            this.keyIndex = this.wordIndex
            break
          case 2:
            this.keyIndex = this.wordIndex - 3
            break
          case 3:
            this.keyIndex = this.wordIndex - 8
            break
        }
        this.isStart = roundInfo.isStart
        this.inputString = roundInfo.object_key
        this.isFinal = roundInfo.isFinal
        if (roundInfo.key_type == 1) {
          this.typeClass = "exam-type"
        } else if (roundInfo.key_type == 0) {
          this.typeClass = "test-type"
        }
        this.checkGame()
      }
    },
    checkGame() {
      if (this.isStart) {
        this.roundTitle = "Round"
        if (this.scores.length == 3) {
          this.btnTitle = "Next"
          // this.isStart = false
          this.btnHide = false
          this.searchHide = true
        } else {
          // this.isStart = false
          this.btnHide = true
          this.searchHide = false
          this.ideaText = ""
        }
        if (this.key_type == 1) {
          this.typeClass = "exam-type"
        } else if (this.key_type == 0) {
          this.typeClass = "test-type"
        }
      } else {
        this.btnTitle = "Start"
        this.searchHide = true
        switch (this.round) {
          case 1:
            this.roundTitle = "Practice"
            this.roundSubTitle =
              "You’ll see an object and type 3 creative uses, 1 at a time, pressing Enter after each one. When you’re ready to start the practice round, click Start."
            this.roundCount = 3
            this.roundClass = "practice"
            break
          case 2:
            this.roundTitle = "Game Time!"
            this.roundCount = 5
            this.roundClass = "exam"
            this.roundSubTitle =
              "Now it’s time to play the game. You’ll play five rounds. You’ll get points based on the originality of your ideas. The better the ideas, the higher your score. Remember to be creative!"
            this.showMark = true
            break
          case 3:
            this.roundTitle = "Final round!"
            this.roundCount = 3
            this.roundClass = "practice"
            this.roundSubTitle =
              "For this last part, you’ll play three rounds of the game, just like before.<br/> You will not see any creativity scores this time."
            break
        }
      }
    },
    async btnClick() {
      this.showMark = false
      if (this.typeClass == "finish-type") {
        this.roundTitle = "Thanks! Please complete this survey now"
        this.roundSubTitle =
          "<a href='https://pennstate.qualtrics.com/jfe/form/SV_6kQzfiT9bI3h8vY' target='_blank'>https://pennstate.qualtrics.com/jfe/form/SV_6kQzfiT9bI3h8vY</a>"
        this.scores = []
        this.isStart = false
        this.btnHide = true
        this.isFinal = true
        console.log("Test ::: ", 236)
      } else {
        if (this.typeClass == "test-type") {
          if (this.isResult) {
            this.scores = await ideaService.getIdeaList()
            this.roundClass = "exam"
            this.typeClass = "finish-type"
            this.roundTitle = "Your creativity scores"
            this.btnTitle = "Finish"
            const scoreList = await ideaService.getScoreList()
            console.log("Score List : ", scoreList)
            excelParser().exportDataFromJSON(scoreList, null, null)
          }
        }

        if (this.isStart && !this.isFinished) {
          if (this.isFinal) {
            if (this.round == 3) {
              if (this.typeClass == "exam-type") {
                this.roundTitle = "Thanks! Please complete this survey now: "
                this.roundSubTitle =
                  "<a href='https://pennstate.qualtrics.com/jfe/form/SV_6kQzfiT9bI3h8vY' target='_blank'>https://pennstate.qualtrics.com/jfe/form/SV_6kQzfiT9bI3h8vY</a>"
                this.scores = []
                this.isStart = false
                this.btnHide = true
                // xcxzcvxcvxc
                const scoreList = await ideaService.getScoreList()
                console.log("Score List : ", scoreList)
                excelParser().exportDataFromJSON(scoreList, null, null)
              } else if (this.typeClass == "test-type") {
                this.btnTitle = "Show Result"
                this.isResult = true
              }
            } else {
              this.round += 1
              this.isStart = false
              await ideaService.setUserRound({
                round: this.round
              })
              this.getExamInformation()
            }
          } else {
            this.wordIndex += 1
            switch (this.round) {
              case 1:
                this.keyIndex = this.wordIndex
                break
              case 2:
                this.keyIndex = this.wordIndex - 3
                break
              case 3:
                this.keyIndex = this.wordIndex - 8
                break
            }
            const keyString = await ideaService.getNextKey({
              objectIndex: this.wordIndex
            })
            this.inputString = keyString
            this.searchHide = false
            this.btnHide = true
            this.scores = []
            this.ideaText = ""
          }
        } else {
          this.isStart = true
          this.checkGame()
        }
      }
    }
  }
}
</script>
