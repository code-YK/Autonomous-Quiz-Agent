export interface Concept {
  name: string
  description: string
  summary: string
}

export interface Question {
  question: string
  related_concept: string
}

export interface RankedQuestion {
  question: string
  difficulty: "Easy" | "Medium" | "Hard"
  related_concept: string
}

export interface QuizResponse {
  concepts: Concept[]
  hierarchy: unknown
  questions: Question[]
  ranked_questions: RankedQuestion[]
  validation_passed: boolean
  validation_feedback: string
  retry_count: number
}
