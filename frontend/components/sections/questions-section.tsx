import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { FileQuestion } from "lucide-react"
import type { RankedQuestion } from "@/lib/types"

interface QuestionsSectionProps {
  questions: RankedQuestion[]
}

const difficultyConfig = {
  Easy: { color: "bg-green-500/10 text-green-700 dark:text-green-400 border-green-500/20", label: "Easy" },
  Medium: { color: "bg-yellow-500/10 text-yellow-700 dark:text-yellow-400 border-yellow-500/20", label: "Medium" },
  Hard: { color: "bg-red-500/10 text-red-700 dark:text-red-400 border-red-500/20", label: "Hard" },
}

export function QuestionsSection({ questions }: QuestionsSectionProps) {
  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <FileQuestion className="h-5 w-5 text-primary" />
        <h3 className="text-lg font-semibold text-foreground">Quiz Questions ({questions.length})</h3>
      </div>

      <div className="grid gap-4">
        {questions.map((q, index) => {
          const config = difficultyConfig[q.difficulty]

          return (
            <Card key={index} className="border-border">
              <CardHeader className="pb-3">
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <span className="text-xs font-mono text-muted-foreground">Q{index + 1}</span>
                      <Badge variant="outline" className={config.color}>
                        {config.label}
                      </Badge>
                    </div>
                    <CardTitle className="text-base leading-relaxed">{q.question}</CardTitle>
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-xs">
                  Related concept: <span className="text-foreground font-medium">{q.related_concept}</span>
                </CardDescription>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </div>
  )
}
